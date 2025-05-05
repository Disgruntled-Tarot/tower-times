from django.contrib import admin
from .models import BlogPost, Tag, Category

admin.site.register(BlogPost)
admin.site.register(Tag)
admin.site.register(Category)
