from django.shortcuts import render


# Create your views here.

def Homepage(request):
    data={
        "name":"hasib",
        "age":34,
    }
    return render(request,"home.html",data)