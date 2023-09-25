import time

from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Container, Log
from .serializers import (
    ContainerSerializer,
    CreateMultipleContainerSerializer,
    LogSerializer,
)
from .services.docker_service import DockerService


@api_view()
def get_all_containers(request):
    if request.query_params:
        state = (
            True
            if request.query_params["state"] == "Running"
            else False
            if request.query_params["state"] == "Finished"
            else None
        )
        if state == None:
            return Response(
                "Unsupported state Type.", status=status.HTTP_400_BAD_REQUEST
            )
        container_list = Container.objects.filter(state=state)
        serializer = ContainerSerializer(container_list, many=True)
        return Response(serializer.data)
    container_list = Container.objects.all()
    serializer = ContainerSerializer(container_list, many=True)
    return Response(serializer.data)


@api_view()
def get_container_by_name(request, name):
    container = get_object_or_404(Container, name=name)
    serializer = ContainerSerializer(container)
    return Response(serializer.data)


@api_view()
def get_container_logs_by_name(request, name):
    log_list = get_list_or_404(Log, name=name)
    serializer = LogSerializer(log_list, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_container(request):
    serializer = ContainerSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    client = DockerService()
    container = client.create(
        serializer.validated_data["name"],
        serializer.validated_data["image"],
        serializer.validated_data.get("envs"),
        serializer.validated_data.get("command"),
    )
    time.sleep(0.3)  # Wait for state of container
    container = client.get(serializer.validated_data["name"])
    serializer.validated_data["state"] = container.attrs["State"]["Running"]

    container_log = Log(**serializer.validated_data)
    container_log.action = "Created"

    serializer.save()
    container_log.save()

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def create_multiple_container(request, name):
    serializer = CreateMultipleContainerSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    main_container = get_object_or_404(Container, name=name)
    container_list = []

    if serializer.data["number"] != len(serializer.data["name_list"]):
        return Response(
            "Number is not equal with length of Name list.",
            status=status.HTTP_400_BAD_REQUEST,
        )

    existing_containers = Container.objects.filter(
        name__in=serializer.data["name_list"]
    )
    if existing_containers:
        existing_containers = [container.name for container in existing_containers]
        return Response(
            f"Container with '{' and '.join(existing_containers)}' name is Already Exists.",
            status=status.HTTP_409_CONFLICT,
        )

    client = DockerService()
    for name in serializer.data["name_list"]:
        docker_container = client.create(
            name,
            main_container.image,
            main_container.envs,
            main_container.command,
        )
        time.sleep(0.3)  # Wait for state of container
        docker_container = client.get(name)

        container = Container(
            name=name,
            image=main_container.image,
            envs=main_container.envs,
            command=main_container.command,
            state=docker_container.attrs["State"]["Running"],
        )

        container_log = Log(
            name=container.name,
            image=container.image,
            envs=container.envs,
            command=container.command,
            state=container.state,
            action="Created",
        )

        container.save()
        container_log.save()
        container_list.append(container.name)
    return Response(container_list, status=status.HTTP_201_CREATED)


@api_view(["PUT"])
def update_container(request, name):
    container = get_object_or_404(Container, name=name)
    serializer = ContainerSerializer(container, data=request.data)
    serializer.is_valid(raise_exception=True)

    if container.name != request.data["name"]:
        return Response(
            "Can not Update name of the container.",
            status=status.HTTP_400_BAD_REQUEST,
        )

    client = DockerService()
    docker_container = client.update(
        serializer.validated_data["name"],
        serializer.validated_data["image"],
        serializer.validated_data.get("envs"),
        serializer.validated_data.get("command"),
    )
    time.sleep(0.3)  # Wait for state of container
    docker_container = client.get(serializer.validated_data["name"])
    serializer.validated_data["state"] = docker_container.attrs["State"]["Running"]

    container_log = Log(
        name=serializer.validated_data["name"],
        image=serializer.validated_data["image"],
        envs=serializer.validated_data["envs"]
        if serializer.validated_data.get("envs")
        else container.envs,
        command=serializer.validated_data["command"]
        if serializer.validated_data.get("command")
        else container.command,
        state=serializer.validated_data["state"],
        action="Updated",
    )

    serializer.save()
    container_log.save()

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["DELETE"])
def delete_container(request, name):
    container = get_object_or_404(Container, name=name)
    client = DockerService()
    client.delete(name)
    container_log = Log(
        name=container.name,
        image=container.image,
        envs=container.envs,
        command=container.command,
        state=False,
        action="Deleted",
    )
    container.delete()
    container_log.save()
    return Response(status=status.HTTP_204_NO_CONTENT)
