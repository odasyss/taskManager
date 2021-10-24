from django.db import models
class Project(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "Project: {}".format(self.name)
