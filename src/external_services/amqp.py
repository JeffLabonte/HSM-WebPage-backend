import json
import time
from typing import Callable, Dict

from pika import BlockingConnection, ConnectionParameters
from pika.channel import Channel


class AMQPService:
    def __init__(self, exchange, callback=None, host="broker", port=5672):
        self.connection = BlockingConnection(
            ConnectionParameters(host=host, port=port),
        )
        self.exchange = exchange
        self.channel = self._init_channel()
        self.queue_name = self._init_queue()
        if callback and callable(callback):
            self._add_callback(callback)

    def _init_channel(self) -> Channel:
        channel = self.connection.channel()
        channel.exchange_declare(
            exchange=self.exchange,
            exchange_type='topic'
        )
        return channel

    def _init_queue(self) -> str:
        result = self.channel.queue_declare('', exclusive=True)
        return result.method.queue

    def _add_callback(self, callback: Callable) -> None:
        if not callable(callback):
            raise RuntimeError("Requires a callable")

        self.channel.basic_consume(
            queue=self.queue_name,
            on_message_callback=callback,
            auto_ack=True,
        )

    def wait_consume(self, timeout=20):
        start_time = time.time()
        while True:
            method_frame, header_frame, body = self.channel.basic_get(
                queue=self.queue_name, auto_ack=False
            )

            if method_frame:
                print(method_frame, header_frame, body)
                self.channel.basic_ack(method_frame.delivery_tag)
                return body

            if time.time() - start_time >= timeout:
                raise TimeoutError()

    def publish(self, topic: str, message: Dict):
        self.channel.basic_publish(
            exchange=self.exchange,
            routing_key=topic,
            body=json.dumps(message),
        )
