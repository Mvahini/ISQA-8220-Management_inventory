from django.contrib import admin

from .models import Client, Project


class ClientList(admin.ModelAdmin):
    list_display = ( 'client_name', 'email', 'phone_number' )
    list_filter = ( 'client_name', 'email')
    search_fields = ('client_name', )
    ordering = ['client_name']


class ProjectList(admin.ModelAdmin):
    list_display = ( 'client_name', 'project_title', 'start_date')
    list_filter = ( 'client_name', 'start_date')
    search_fields = ('client_name', )
    ordering = ['client_name']



admin.site.register(Client, ClientList)
admin.site.register(Project, ProjectList)
