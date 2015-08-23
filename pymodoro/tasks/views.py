from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from forms import UserForm

def home(request):
    print "HOME"
    return render(request, 'tasks/home.html')

@login_required
def index(request):
    print "INDEX"
    return render(request, 'tasks/index.html')

def create_user(request):
    print "CREATE_USER"
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            return HttpResponseRedirect('/')
    else:
        form = UserForm()
    return render(request, 'tasks/create_user.html', {'form': form})
