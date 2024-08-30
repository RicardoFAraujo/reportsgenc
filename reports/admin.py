# reports/admin.py

from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile, Company, Report

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class UserAdmin(admin.ModelAdmin):
    inlines = [UserProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'description')
