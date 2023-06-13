# profiles/models.py

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pics/')

