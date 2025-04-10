from django.contrib import admin
from .models import Car, Photo, Financing, Message, User

# Register your models here.

admin.site.register(User)
admin.site.register(Car)
admin.site.register(Photo)
admin.site.register(Financing)
admin.site.register(Message)
