from django.contrib import admin

# Register your models here.
from directory.models import Doctor, Specialty

admin.site.register(Doctor)
admin.site.register(Specialty)
