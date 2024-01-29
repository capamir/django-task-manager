from django.contrib import admin
from .models import Project, Task, Review
# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created')
    search_fields = ('title',)
    raw_id_fields = ('created_by',)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'assigned_to', 'project', 'completed', 'created')
    search_fields = ('title',)
    list_filter = ('completed',)
    raw_id_fields = ('assigned_to', 'project')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('feedback', 'task', 'project', 'reviewer', 'created', 'is_reply')
    search_fields = ('feedback',)
    list_filter = ('is_reply',)
    raw_id_fields = ('project', 'task', 'reviewer')


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Review, ReviewAdmin)
