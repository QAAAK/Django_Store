from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models he
class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)

