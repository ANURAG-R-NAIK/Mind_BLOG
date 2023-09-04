from django.contrib import admin
from .models import Post #import post from models.py

admin.site.register(Post) 
# we register the model created to be accessed from the admin page later