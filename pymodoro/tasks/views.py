from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext

from .models import Task

@login_required
def index(request):
    task_list = Task.objects.order_by('id')[:5]
    context = RequestContext(request, {
        'task_list': task_list,
    })
    return render(request, 'tasks/index.html', context)

@login_required
def detail(request, task_id):
    return HttpResponse("You're looking at task %s." % task_id)

@login_required
def results(request, task_id):
    response = "You're looking at the results of task %s."
    return HttpResponse(response % task_id)

def vote(request, task_id):
    return HttpResponse("You're voting on task %s." % task_id)
