from django.db import models


class EventType(models.TextChoices):
    CREDIBLE = "Credible"
    RANDOM = "Random"
    IMPOSSIBLE = "Impossible"


class EventCategory(models.TextChoices):
    INFO = "Info"
    ATTENTION = "Attention"
    ALARM = "Alarm"
