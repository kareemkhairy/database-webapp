# Correct import statement in myapp/admin.py

from django.contrib import admin
from .models import UserInfo  # Adjust the import path as per your project structure

admin.site.register(UserInfo)
