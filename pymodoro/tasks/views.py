from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from forms import UserForm
from models import Task

POMODORO_TIME = 0.05

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
    print "LIST"
    print request.user.id
    user = User.objects.get(pk=request.user.id)
    tasks = Task.objects.filter(user=user)
    return render(request, template_name, {'tasks': tasks})

@login_required
def create_task(request):
    print "CREATE"
    if request.method == 'POST':
        task_name = request.POST['taskname']
        if task_name:
            user = User.objects.get(pk=request.user.id)
            task = Task.objects.create(user=user)
            task.name = task_name
            task.save()
    return redirect('home')

@login_required
def get_task(request, task_id, template_name='tasks/task.html'):
    task = Task.objects.get(pk=task_id)
    return render(request, template_name, {'task': task})

@login_required
def update_task(request, task_id, template_name='tasks/update_tasks.html'):
    task = Task.objects.get(pk=task_id)
    if request.method == "GET":
        return render(request, template_name, {'task': task})
    
    if request.method == "POST":
        task_name = request.POST['taskname']
        task.name = task_name
        task.save()
    return redirect('home')

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('home')

@login_required
def start_task(request, task_id, template_name='tasks/start.html'):
    task = Task.objects.get(pk=task_id)
    return render(request, template_name, {'task': task, 'POMODORO_TIME': POMODORO_TIME})

@login_required
def finish_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.pomodoros += 1
    task.total_time += 25
    task.save()
    return redirect('home')
