from django.contrib import admin
from .models import Student, Teacher
# Register your models here.

admin.site.site_header = "Rapidier"

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "phone_number")
    
    exclude = ('groups', 'user_permissions', 'is_active', 'is_superuser', 'last_login', "password", "is_staff")

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "phone_number")
    
    exclude = ('groups', 'user_permissions', 'is_active', 'is_superuser', 'last_login', "password")
