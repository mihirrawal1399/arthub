from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Photo)                  # Admin can access Photo table
admin.site.register(Photographer)           # Admin can access Photographer table
admin.site.register(Categories)             # Admin can access Category table
# admin.site.register(Coll)
admin.site.register(Order)

admin.site.site_header = 'ARTHUB Administration'
