from django.contrib import admin

from .models import ClientDetail,ProjectDetail

class ClientList(admin.ModelAdmin):
    list_display = ( 'client_first_name', 'client_last_name', 'phone_number' )
    list_filter = ( 'client_first_name', 'client_last_name')
    search_fields = ('client_first_name', )
    ordering = ['client_first_name']


admin.site.register(ClientDetail)


class ProjectList(admin.ModelAdmin):
    list_display = ( 'project_title', 'description', 'cost_estimation' )
    list_filter = ( 'project_title', 'description')
    search_fields = ('project_title', )
    ordering = ['project_title']


admin.site.register(ProjectDetail)
