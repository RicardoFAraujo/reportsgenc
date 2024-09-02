# reports/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, Company, Report
from .forms import UserCreationForm

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    inlines = [UserProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'description')


