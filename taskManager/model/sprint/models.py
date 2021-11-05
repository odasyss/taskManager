from django.db import models
from django.db.models.base import Model
from taskManager.model.project.models import Project

class Sprint(models.Model):
    name = models.CharField(max_length=50, blank=True, default='')
    description = models.TextField(blank=True, default='')
    start = models.DateTimeField(unique=True)
    Duration= models.DurationField()
    end = models.DateField(unique=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False)


    def __str__(self):
        return self.name or ('Sprint ending %s') % self.end

    class Meta:
        ordering = ['name']

