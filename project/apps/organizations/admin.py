from django.contrib import admin

from project.apps.organizations.models import Organization


class OrganizationAdmin(admin.ModelAdmin):
    fields = ('name', 'created_at',)
    list_display = ('name', 'created_at',)
    search_fields = ('name',)
    readonly_fields = ('created_at',)


admin.site.register(Organization, OrganizationAdmin)
