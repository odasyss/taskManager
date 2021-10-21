from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    STATUS_TODO = 1
    STATUS_IN_PROGRESS = 2
    STATUS_TESTING = 3
    STATUS_DONE = 4

    STATUS_CHOICES = (
        (STATUS_TODO, ('Not Started')),
        (STATUS_IN_PROGRESS, ('In Progress')),
        (STATUS_TESTING, ('Testing')),
        (STATUS_DONE, ('Done')),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    projectname = models.CharField(max_length=200, default="")
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)   
    sprint = models.CharField(max_length=200, default="")
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=STATUS_TODO)
    subtask = models.ForeignKey('self',on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']

