from django.contrib import admin
from . import models 
# imported the current directory models

# Register your models here.

admin.site.register(models.car)
# registering the car model in the admin interface
# for registering a model with respect to the admin 
admin.site.register(models.Review)