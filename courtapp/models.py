from django.db import models
from userapp.models import *
from django.contrib.auth.models import AbstractUser


class Law(models.Model):
    court = models.ForeignKey(Register, on_delete=models.CASCADE,null=True, related_name='court')
    name = models.CharField(max_length=50, null=True)
    ipc = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=100000, null=True)
    year_of_act = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)