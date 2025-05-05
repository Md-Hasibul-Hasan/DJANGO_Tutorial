from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .models import User

# Create your views here.

def info(request):
    data=User.objects.all()
    return render(request, "info.html", {"data":data})

def update(request,x):
    user=User.objects.get(id=x)
    if request.method == "POST":
        # user.name = request.POST.get("name")
        user.email = request.POST.get("email")
        user.password = request.POST.get("password")
        user.save()
        messages.success(request, "updated successfully")
    return render(request, "update.html", {"user":user})

def delete(request,x):
    user=User.objects.get(id=x)
    user.delete()
    return redirect("info")

def signup(request):
    if request.method == "POST":
        nm=request.POST.get("name")
        em=request.POST.get("email")
        pass1=request.POST.get("password")
        pass2=request.POST.get("confirm password")

        if User.objects.filter(name=nm).exists():
            messages.warning(request, "name already exists")
        elif pass1!=pass2:
            messages.error(request, "pass dont match")
        else:
            User.objects.create(name=nm, email=em, password=pass1)
            messages.success(request, "success done ")
    return render(request, "signup.html")


def login(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")

        # if user.objects.filter(name=name, password=password).exists():
        try:
            dt=User.objects.get(name=name,password=password)
            request.session["userid"]=dt.id
            return redirect("profile")
        except:
            return HttpResponse("login failed")
        
    return render(request, "login.html")

def profile(request):
    x=request.session.get("userid")
    dt=User.objects.get(id=x)
    if request.method =="POST":
        # dt.name= request.POST.get("name")
        dt.email= request.POST.get("email")
        dt.password= request.POST.get("password")
        dt.save()
    return render(request, "profile.html",{"user":dt})

def logout(request):
    try:
        del request.session['userid']
    except KeyError:
        pass
    return redirect("signup")