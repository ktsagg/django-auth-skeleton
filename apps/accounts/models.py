from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom User class
    Extends the default User class to define more model fields.
    """
    pass
    # age = models.IntegerField(blank=True,null=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
