from django.db import models
from django.contrib.auth.models import User
from .const import EventType, EventCategory


class Tag(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Event(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=10, choices=EventType.choices)
    description = models.TextField()
    category = models.CharField(max_length=10, choices=EventCategory.choices)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.description
