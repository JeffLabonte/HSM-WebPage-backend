from uuid import uuid4

from rest_framework import serializers


class ScriptWriteSerializzer(serializers.Serializer):
    data = serializers.CharField(required=True, write-only=True)
    transaction_id = serializers.CharField(required=True, default=uuid4())
    method = serializers.ChoiceField(choices=[
        ("PUT", "PUT"),
        ("POST", "POST"),
        ("PATCH", "PATCH"),
    ])


    class Meta:
        fields = (
            "data",
            "transaction_id",
            "method",
        )
        default_fields = (
            "data",
            "transaction_id",
            "method"
        )
