from django.db import models

# Create your models here.
class User(Models.Model):
    user_name = models.CharField(max_length=20)
    user_name = models.EmailField(unique=True)
    user_password = models.CharField(max_length=100)
    user_validate = models.BooleanField(default=False)