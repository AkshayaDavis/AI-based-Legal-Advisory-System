from django.db import models
from django.contrib.auth.models import AbstractUser
class Register(AbstractUser):
    usertype = models.CharField(max_length=50, default="admin")
    phone = models.CharField(max_length=15, null=True)  # Changed to CharField
    image = models.ImageField(upload_to='uploads/', null=True)
    barcouncil_number = models.CharField(max_length=15, null=True)
    specialization = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=100, null=True)
    bio = models.TextField(max_length=500, null=True)
    qualification = models.CharField(max_length=50, null=True)
    experience = models.CharField(max_length=10, null=True)
    availability_from = models.TimeField(max_length=10, null=True)
    availability_to = models.CharField(max_length=10, null=True)
    court_jurisdiction = models.CharField(max_length=50, null=True)
    court_type = models.CharField(max_length=50, null=True)
    place = models.CharField(max_length=50, null=True)

class Reset(models.Model):
    otp = models.CharField(max_length=6, null=True)
    user = models.ForeignKey(Register, on_delete=models.CASCADE,null=True)
    otp_created_at = models.DateTimeField(auto_now_add =True)