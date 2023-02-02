from django.contrib import admin
from .models import *

# Register the models that we want to watch in the admin user interface.
admin.site.register([Question, Choice])
