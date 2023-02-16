from django.contrib import admin
from .models import Post,Certificate

admin.site.register((Post, Certificate))
