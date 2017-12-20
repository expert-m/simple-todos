from django.contrib import admin

from project.apps.tasks.models import Task


class TaskAdmin(admin.ModelAdmin):
    fields = ('description', 'organization', 'user', 'created_at',)
    list_display = ('description', 'organization', 'created_at',)
    search_fields = ('description',)
    readonly_fields = ('created_at',)
    raw_id_fields = ('organization', 'user',)


admin.site.register(Task, TaskAdmin)
