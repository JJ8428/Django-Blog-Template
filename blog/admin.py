from django.contrib import admin
from .models import Post

# Register your models here so they appear on admin
admin.site.register(Post) # Now the admin website will show the Post DB
# User is provided by dJango, so it is auto registered