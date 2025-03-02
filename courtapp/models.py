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

class Jury(models.Model):
    usertype = models.CharField(max_length=50, default="jury")
    court = models.ForeignKey(Register, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    specialization = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    trial = models.ForeignKey(Law, on_delete=models.CASCADE,null=True, related_name='trial_schedule')
    jury = models.ForeignKey(Jury, on_delete=models.CASCADE,null=True, related_name='jury_schedule')
    scheduled_date = models.DateField(null=True)
    scheduled_time = models.TimeField(null=True)
    status = models.CharField(max_length=50, default="Pending")
    reject_reason = models.TextField(max_length=100000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)