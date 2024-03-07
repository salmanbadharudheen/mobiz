from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLES = (
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('admin', 'Admin'),
        ('editor', 'Editor'),
    )
    role = models.CharField(max_length=10, choices=ROLES, default='student')
    nationality = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    mobile = models.CharField(max_length=15, blank=True)
    email=models.EmailField(unique=True)


    def __str__(self):
        return self.username
