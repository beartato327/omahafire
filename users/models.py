from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    #add attributes here
    pass
    
    def __str__(self):
        return self.email