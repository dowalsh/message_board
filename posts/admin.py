from django.contrib import admin

# Register your models here.
from .models import Post # This line is added to import the Post model.

admin.site.register(Post) # This line is added to register the Post model with the admin site.