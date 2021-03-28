from uuid import uuid4

from rest_framework import serializers

REPO_URL_REGEX = r"^(git@github.com:)[A-Za-z0-9-_.]+/[A-Za-z0-9-_.]+.git$"


class RepositorySerializer(serializers.Serializer):
    repo_url = serializers.RegexField(regex=REPO_URL_REGEX)
    version = serializers.CharField(default="main")
    execution = serializers.CharField(required=True)


class ScriptDataSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, min_length=1, max_length=40)
    repository = RepositorySerializer()


class ScriptWriteSerializer(serializers.Serializer):
    data = ScriptDataSerializer(
        required=True,
    )
    transaction_id = serializers.CharField(
        default=uuid4(),
    )
    method = serializers.ChoiceField(
        choices=[
            ("PUT", "PUT"),
            ("POST", "POST"),
            ("PATCH", "PATCH"),
        ]
    )


    class Meta:
        fields = (
            "data",
            "transaction_id",
            "method",
        )
        default_fields = (
            "data",
            "transaction_id",
            "method",
        )
