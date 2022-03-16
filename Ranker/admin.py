from django.contrib import admin
from .models import Rating, Professor, Module

admin.site.register(Rating)
admin.site.register(Professor)
admin.site.register(Module)