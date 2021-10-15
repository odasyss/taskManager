from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _



class Sprint(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    end = models.DateField(unique=True)

    def __str__(self):
        return self.name or _('Sprint ending %s') % self.end

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    # sprint = models.ForeignKey(Sprint, blank=True, null=True)
    order = models.SmallIntegerField(default=0)
    started = models.DateField(blank=True, null=True)
    due = models.DateField(blank=True, null=True)
    completed = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name