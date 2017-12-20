from django.db import models

from project.apps.organizations.models import Organization
from project.apps.users.models import User


class Task(models.Model):
    description = models.CharField(max_length=500)
    user = models.ForeignKey(User, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    organization = models.ForeignKey(Organization, related_name='tasks')

    def __unicode__(self):
        return self.description

    def __str__(self):
        return self.description
