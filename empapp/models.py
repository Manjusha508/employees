from django.db import models
import json

from django.utils import timezone
import uuid
from django.db import models

def generate_photo_upload_path(instance, filename):
    return f'photos/{uuid.uuid4()}/{filename}'


# In the migration prompt, you can enter `timezone.now()`

class Employee(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    email = models.EmailField(default='default@example.com')  # <- Add default
    gender = models.CharField(max_length=10,null=True, blank=True)
    phoneNo = models.CharField(max_length=15,null=True, blank=True)
    hno = models.CharField(max_length=50,null=True, blank=True)
    street = models.CharField(max_length=100,null=True, blank=True)
    city = models.CharField(max_length=100,null=True, blank=True)
    state = models.CharField(max_length=100,null=True, blank=True)
    companyName = models.CharField(max_length=100,null=True, blank=True)
    fromDate = models.DateField(default=timezone.now)
    toDate = models.DateField(default=timezone.now)
    qualificationName = models.JSONField(default=dict)
    description = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=100,null=True, blank=True)
    age = models.IntegerField(default=0)  # Set a default value like 0

    percentage = models.FloatField(default=0)
    addressDetails = models.JSONField(default=dict)


    qualifications = models.JSONField(default=dict)
    workExperience = models.JSONField(default=dict)
    projects = models.JSONField(default=dict)
    photo = models.ImageField(upload_to=generate_photo_upload_path, default='photos/default.jpeg')
