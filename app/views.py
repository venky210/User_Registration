from django.shortcuts import render

# Create your views here.
from app.forms import *

from app.models import *

from django.http import HttpResponse

from django.core.mail import send_mail



def registration(request):
    UFO=userform()
    PFO=Profileform()
    d={'user':UFO,'profile':PFO}
    if request.method=='POST' and request.FILES:
        ufd=userform(request.POST)
        pfd=Profileform(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            MUFDO=ufd.save(commit=False)
            pw=ufd.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()
            MPFDO=pfd.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
            send_mail('registration','registrations is successfully','venkateshkolluboina210@gmail.com',[MUFDO.email],fail_silently=False)
            return HttpResponse('Registration is successfully')
        else:
            return HttpResponse('invaild data')
    return render(request,'registration.html',d)



