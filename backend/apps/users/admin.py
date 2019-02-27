from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from apps.users.models import User
from apps.users.forms import UserChangeForm, UserCreationForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['full_name', 'email']
    fieldsets = [
        ['Auth', {'fields': ['email', 'password']}],
        ['Personal info', {'fields': ['last_name', 'first_name', 'avatar', 'nationality', 'age', 'address', 'phone_number']}],
        ['Work related info', {'fields': ['sector', 'skills', 'salary', 'started', 'ended', 'is_employee', 'days_in_company']}],
        ['Settings', {'fields': ['groups', 'is_archived', 'is_admin', 'is_active', 'is_staff', 'is_superuser']}],
        ['Important dates', {'fields': ['last_login', 'registered_at']}],
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [[None, {'classes': ['wide'], 'fields': [
        'email', 'first_name', 'last_name', 'password1', 'password2']}], ]
    search_fields = ['email']
    ordering = ['email']
    readonly_fields = ['last_login', 'registered_at', 'days_in_company']


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
# Unregister the Group model from admin.
admin.site.unregister(Group)
