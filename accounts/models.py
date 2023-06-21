from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    ROLES = (
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('admin', 'Admin'),
        ('editor', 'Editor'),
    )

    role = models.CharField(max_length=50, choices=ROLES)
    country = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
