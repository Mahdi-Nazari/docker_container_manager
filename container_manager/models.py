from django.db import models


class Container(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.CharField(max_length=255)
    envs = models.JSONField(default=dict, blank=True)
    command = models.CharField(max_length=255, default="", blank=True)
    state = models.BooleanField()
    last_update = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]


class Log(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    envs = models.JSONField(default=dict)
    command = models.CharField(max_length=255, default="")
    state = models.BooleanField()
    action = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
