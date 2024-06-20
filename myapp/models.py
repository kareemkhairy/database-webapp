from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.hashers import make_password

class UserInfo(models.Model):
    username = models.CharField(max_length=150, unique=True, validators=[UnicodeUsernameValidator()])
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, validators=[MinLengthValidator(8)])  # Example of minimum length validation
    date_of_birth = models.DateField()

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        # Hash the password before saving
        self.password = make_password(self.password)
        super().save(*args, **kwargs)
