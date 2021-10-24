from django.db import models
from taskManager.model.project.models import Project


class Sprint(models.Model):
    name = models.CharField(max_length=50, blank=True, default='')
    description = models.TextField(blank=True, default='')
    start = models.DateTimeField(unique=True)
    Duration= models.DurationField()
    end = models.DateField(unique=True)

    def __str__(self):
        return self.name or ('Sprint ending %s') % self.end