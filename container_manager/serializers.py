from rest_framework import serializers

from .models import Container, Log


class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = [
            "name",
            "image",
            "envs",
            "command",
            "state",
            "last_update",
            "created_at",
        ]

    state = serializers.SerializerMethodField(method_name="set_state", read_only=True)

    def set_state(self, container):
        return "Running" if container.state == True else "Finished"


class CreateMultipleContainerSerializer(serializers.Serializer):
    number = serializers.IntegerField(min_value=1)
    name_list = serializers.ListField(child=serializers.CharField(max_length=255))


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = [
            "name",
            "image",
            "envs",
            "command",
            "state",
            "action",
            "created_at",
        ]

    state = serializers.SerializerMethodField(method_name="set_state")

    def set_state(self, log):
        return "Running" if log.state == True else "Finished"
