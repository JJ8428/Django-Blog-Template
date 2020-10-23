from django.contrib import admin
from .models import Profile

# Register your models here.
# DO NOT FORGET TO REGISTER YOUR MODEL, OTHERWISE IT WILL NOT APPEAR ON ADMIN
admin.site.register(Profile)