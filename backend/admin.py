from django.contrib import admin
from .models import Post,TopPost

admin.site.register((Post, TopPost))
