from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=50)
    start = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return "Project: {}".format(self.name)

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

class Task(models.Model):
    STATUS_CHOICES = (
        ('Todo', 'Todo'),
    ('Progress', 'Progress'),
    ('Review', 'Review'),
    ('Done', 'Done'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)   
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)
    subtask = models.ForeignKey('self',on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Action(models.Model):
    name = models.CharField(max_length=50)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, blank=True, null=True)

    def str(self):
        return self.name