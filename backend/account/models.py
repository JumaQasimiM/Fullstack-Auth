from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Account(AbstractUser):
    USER_ROLE = [
        ('admin','Admin'),
        ('viewer','Viewer'),
        ('company','Company'),
        ('job_search','Looking for a job'),

    ]
    avatar = models.ImageField(upload_to='avatars/',null=True,blank=True)
    role = models.CharField(max_length=20,choices=USER_ROLE,default='job_search')
    bio = models.TextField(null=True, blank=True)
    field_of_stady = models.CharField(max_length=255,null=True,blank=True)
    skills = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.first_name