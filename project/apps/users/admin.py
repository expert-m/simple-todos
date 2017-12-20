from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from project.apps.users.models import User


class NewUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_staff',)
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        (_('Permissions'), {'fields': (
            'is_active', 'is_staff', 'is_superuser', 'groups',
            'user_permissions', 'organizations',)}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    search_fields = ('email',)
    filter_horizontal = ('groups', 'user_permissions', 'organizations',)


admin.site.register(User, NewUserAdmin)
