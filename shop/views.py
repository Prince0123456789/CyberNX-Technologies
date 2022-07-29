from django.http import HttpResponse
from django.shortcuts import render
from shop import models
def signup(request):
    try:
        usr = models.user()
        usr.fname = request.POST['fname']
        usr.lname = request.POST['lname']
        usr.phoneno = request.POST['phoneno']
        usr.save()
        return HttpResponse("Signed Up Successfully")
    except:
        err={'error':'Something Went Wrong'}
        return HttpResponse(err[0])

def login(request):
    try:
        usr = models.user.objects.get(phoneno=request.POST['phoneno'])
        if usr:
            request.session['user']=request.POST['phoneno']
        return HttpResponse("Log in Successfully")
    except:
        err={'error':'Something Went Wrong'}
        return HttpResponse(err[0])

def add_profilephoto(request):
    if request.POST['phoneno'] == request.session.keys():
        user = models.user.objects.get(phoneno=request.POST['phone'])
        profile = models.profile(user = user)
        profile.save()
