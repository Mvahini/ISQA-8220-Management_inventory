from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect



now = timezone.now()
def home(request):
   return render(request, 'mi/home.html',
                 {'mi': home})

@login_required
def client_list(request):
    client = Client.objects.all
    return render(request, 'mi/client_list.html',
                  {'clients': client})

@login_required
def client_edit(request, pk):
   client = get_object_or_404(Client, pk=pk)
   if request.method == "POST":
       # update
       form = ClientForm(request.POST, instance=client)
       if form.is_valid():
           client = form.save(commit=False)
           client.updated_date = timezone.now()
           client.save()
           client = Client.objects.all
           return render(request, 'mi/client_list.html',
                         {'clients': client})
   else:
        # edit
       form = ClientForm(instance=client)
   return render(request, 'mi/client_edit.html', {'form': form})

@login_required
def client_delete(request, pk):
   client = get_object_or_404(Client, pk=pk)
   client.delete()
   return redirect('mi:client_list')


@login_required
def project_list(request):
   projects = Project.objects.all
   return render(request, 'mi/project_list.html', {'projects': projects})


@login_required
def project_new(request):
   if request.method == "POST":
       form = ProjectForm(request.POST)
       if form.is_valid():
           project = form.save(commit=False)
           project.created_date = timezone.now()
           project.save()
           projects = Project.objects.all
           return render(request, 'mi/project_list.html',
                         {'projects': projects})
   else:
       form = ProjectForm()
       # print("Else")
   return render(request, 'mi/project_new.html', {'form': form})


@login_required
def project_edit(request, pk):
   project = get_object_or_404(Project, pk=pk)
   if request.method == "POST":
       form = ProjectForm(request.POST, instance=project)
       if form.is_valid():
           project = form.save()
           project.updated_date = timezone.now()
           project.save()
           projects = Project.objects.all
           return render(request, 'mi/project_list.html', {'projects': projects})
   else:
       # print("else")
       form = ProjectForm(instance=project)
   return render(request, 'mi/project_edit.html', {'form': form})


@login_required
def project_delete(request, pk):
   project = get_object_or_404(Project, pk=pk)
   project.delete()
   return redirect('mi:project_list')


def forgot_password(request):
    if request.method == 'POST':
        return render(request, 'registration/password_reset_complete.html')
    else:
        return render(request, 'registration/password_reset_complete.html')


@login_required
def summary(request, pk):
    client = Client.objects.filter(client_name=pk)
    project = Project.objects.filter(client_name=pk)
    return render(request, 'mi/summary.html', {'clients': client, 'projects': project,})

