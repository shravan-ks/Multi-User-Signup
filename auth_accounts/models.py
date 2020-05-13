from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from new_auth import settings


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200)
    is_agent = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username