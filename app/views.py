from django.shortcuts import render

# Create your views here.
from app.forms import *

from app.models import *

def registration(request):
    UFO=userform()
    PFO=Profileform()
    d={'user':UFO,'profile':PFO}
    return render(request,'registration.html',d)