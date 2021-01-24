FROM python:3.9-buster
LABEL maintainer="Jeff Labonte <grimsleepless@protonmail.com>"

WORKDIR /opt

COPY docker-entrypoint.sh /opt/

COPY requirements.txt /opt/
RUN pip install -r requirements.txt

COPY src/ /opt/src/


ENTRYPOINT [ "./docker-entrypoint.sh" ]
