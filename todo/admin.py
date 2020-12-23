from django.contrib import admin
from .models import Todo

# Register your models here.

# Register The Todo Model In the Admin View.
admin.site.register(Todo)