from django.shortcuts import render
from form.forms import Registration

# Create your views here.

def register(request):
    fm = Registration()
    return render(request, 'form/registration.html',{"f":fm})

# def register(request):
    # if request.method=='POST':
    #     f = Registration(request.POST)
    #     print(request.POST)
    # else:
    #     f = Registration()
        
    # return render(request, 'form/registration.html',{"f":f}) 