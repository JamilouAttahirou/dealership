from django.contrib import admin

# Register your models here.

from .models import Car, Photo, Financing, Message, User

admin.site.register(User)
admin.site.register(Car)
admin.site.register(Photo)
admin.site.register(Financing)
admin.site.register(Message)