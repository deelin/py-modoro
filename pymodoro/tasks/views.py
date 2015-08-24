from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from forms import UserForm
from models import Task

def home(request):
    if request.user.is_authenticated():
        return redirect('list')
    return render(request, 'tasks/home.html')

def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            # Save new user
            User.objects.create_user(**form.cleaned_data)

            # Auth user and login user. Redirect to home
            post = request.POST
            user = authenticate(username=post['username'], password=post['password'])
            login(request, user)
            return redirect('tasks.views.home')
    else:
        form = UserForm()
    return render(request, 'tasks/create_user.html', {'form': form})

@login_required
def list_tasks(request, template_name='tasks/list_tasks.html'):
    print request.user.id
    user = User.objects.get(pk=request.user.id)
    tasks = Task.objects.filter(user=user)
    return render(request, template_name, {'tasks': tasks})

@login_required
def create_task(request):
    if request.method == 'POST':
        task_name = request.POST['taskname']
        if task_name:
            user = User.objects.get(pk=request.user.id)
            task = Task.objects.create(user=user)
            task.name = task_name
            task.save()
    return redirect('home')

@login_required
def get_task(request, template_name='tasks/get_tasks.html'):
    return render(request, template_name)

@login_required
def update_task(request, template_name='tasks/update_tasks.html'):
    return render(request, template_name)

@login_required
def delete_task(request, template_name='tasks/delete_tasks.html'):
    return render(request, template_name)
