from django import forms
from .models import Client, Project
from django.contrib.auth.models import User

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('client_name', 'email', 'address', 'city', 'state', 'zipcode', 'phone_number')

class ProjectForm(forms.ModelForm):
   class Meta:
       model = Project
       fields = ('client_name', 'project_title','description', 'start_date', 'end_date', 'cost_estimation', 'status')

