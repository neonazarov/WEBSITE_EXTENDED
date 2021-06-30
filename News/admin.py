from django.contrib import admin
from .models import *


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
