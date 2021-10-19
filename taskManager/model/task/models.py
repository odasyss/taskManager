from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    projectname = models.CharField(max_length=200, default="")
    summary = models.TextField(null=True, blank=True)
    label = models.CharField(max_length=200, blank=True)
    sprint = models.CharField(max_length=200, default="")
    status = models.CharField(max_length=200, default="")
    subtask = models.ForeignKey('self',on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']

