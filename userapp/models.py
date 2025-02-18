from django.db import models
from django.contrib.auth.models import AbstractUser
class Register(AbstractUser):
    usertype = models.CharField(max_length=50, default="admin")
    phone = models.CharField(max_length=15, null=True)  # Changed to CharField
    image = models.ImageField(upload_to='uploads/', null=True)
    barcouncil_number = models.CharField(max_length=15, null=True)
    specialization = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=100, null=True)
    bio = models.TextField(max_length=1000, null=True)
    qualification = models.CharField(max_length=50, null=True)
    experience = models.CharField(max_length=10, null=True)
    consultation_mode = models.CharField(max_length=50, null=True)
    court_jurisdiction = models.CharField(max_length=50, null=True)
    court_type = models.CharField(max_length=50, null=True)
    place = models.CharField(max_length=50, null=True)
    is_approved = models.BooleanField(default=False)

class Reset(models.Model):
    otp = models.CharField(max_length=6, null=True)
    user = models.ForeignKey(Register, on_delete=models.CASCADE,null=True)
    otp_created_at = models.DateTimeField(auto_now_add =True)

class Bookings(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE,null=True)
    lawyer = models.ForeignKey(Register, on_delete=models.CASCADE, related_name='lawyer',null=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="Pending")
    is_approved = models.BooleanField(default=False)
    content = models.FileField(upload_to='uploads/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Chat(models.Model):
    sender = models.ForeignKey(Register, on_delete=models.CASCADE, related_name='sender',null=True)
    receiver = models.ForeignKey(Register, on_delete=models.CASCADE, related_name='receiver',null=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    message = models.TextField(max_length=1000, null=True)
    response = models.TextField(max_length=1000, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Law(models.Model):
    court = models.ForeignKey(Register, on_delete=models.CASCADE,null=True, related_name='court')
    name = models.CharField(max_length=50, null=True)
    ipc = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=1000, null=True)
    year_of_act = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)