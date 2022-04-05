from django.contrib import admin
from fees.models  import  Contact
from fees.models import Client


# Register your models here.
admin.site.register(Contact)
admin.site.register(Client)