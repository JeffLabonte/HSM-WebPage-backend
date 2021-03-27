from rest_framework import serializers


class ScriptWriteSerializzer(serializers.Serializer):
    data = serializers.CharField(required=True, write-only=True)
