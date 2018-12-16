from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    name = models.CharField(blank = True, max_length = 255)
    karma = models.IntegerField(default = 0)
    is_active = models.BooleanField(default = True)
    is_moderator = models.BooleanField(default = False)

    def __str__(self):
        return self.email