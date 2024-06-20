from django.contrib import admin
from .models import carbooking
from .models import hotelbooking
from .models import tourbooking

# Register your models here.
admin.site.register(carbooking)
admin.site.register(hotelbooking)
admin.site.register(tourbooking)