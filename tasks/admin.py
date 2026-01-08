from django.contrib import admin
from tasks.models import Tasks

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ( 
        'title',
        'description',
        'created_at',
        'is_completed'
    )

admin.site.register(Tasks, TaskAdmin )