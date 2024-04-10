from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title']
    filter_horizontal = ['categories']

admin.site.register(Post, PostAdmin)
