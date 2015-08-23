from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    console.log("HELLO!")
    return HttpResponse("hello!")

def create_user(request):
    console.log("CREATE USER")
    return HttpResponse("sup")
