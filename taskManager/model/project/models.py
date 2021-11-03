from django.db import models
class Project(models.Model):
    name = models.CharField(max_length=50)
    start = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return "Project: {}".format(self.name)
