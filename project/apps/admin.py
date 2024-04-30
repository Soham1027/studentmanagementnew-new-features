from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
#class UserModel(UserAdmin):
#   list_display=['username','p_type']
admin.site.register(STAaccounts)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(timetable)

