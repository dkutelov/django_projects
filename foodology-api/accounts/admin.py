from django.contrib import admin
from .models import User, Profile, DefaultDeliveryAddress

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(DefaultDeliveryAddress)