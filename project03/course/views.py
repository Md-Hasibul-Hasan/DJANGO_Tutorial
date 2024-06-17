from django.shortcuts import render


# Create your views here.

def learn(request):
    return render(request,"course/course.html")

def dyna(request):
    data={
        "name":"dj",
        "tk":1000,
    }
    
    return render(request,"course/course.html",data)


