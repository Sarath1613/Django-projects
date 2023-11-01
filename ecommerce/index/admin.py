from django.contrib import admin

# Register your models here.

from .models import offers,picture,client,contactform

admin.site.register(offers)
admin.site.register(picture)
admin.site.register(client)
admin.site.register(contactform)
