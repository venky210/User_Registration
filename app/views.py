from django.shortcuts import render

# Create your views here.
from app.forms import *

from app.models import *

from django.http import HttpResponse,HttpResponseRedirect

from django.urls import reverse

from django.core.mail import send_mail

from django.contrib.auth import authenticate,login




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



def home_page(request):
    if request.session.get('username'):
        un=request.session.get('username')
        d={'username':un}
        return render(request,'home_page.html',d)
    return render(request,'home_page.html')







def user_login(request):
    if request.method=='POST':
        un=request.POST['un']
        pw=request.POST['pw']
        AUO=authenticate(username=un,password=pw)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=un
            return HttpResponseRedirect(reverse('home_page'))
        else:
            return HttpResponse('none')
        
    return render (request,'user_login.html')