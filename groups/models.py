from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='social_groups',
                                        related_query_name='social_group',
                                          blank=True)