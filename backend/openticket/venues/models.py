from django.db import models
from accounts.models import Organization
from openticket.utils import TrackedMixin


class Venue(TrackedMixin, models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.TextField()
    location = models.TextField()

    class Meta:
        unique_together = ("organization", "name")


class Event(TrackedMixin, models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ("venue", "datetime")


class Seat(TrackedMixin, models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    identifier = models.TextField()

    class Meta:
        unique_together = ("event", "identifier")
