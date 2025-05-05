from django.shortcuts import render,HttpResponseRedirect
from student.forms import Registration

# Create your views here.
def home(request):
    if request.method=='POST':
        fm=Registration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            pw=fm.cleaned_data['password']
            print('Name:',nm)
            print('Password:',pw)
            return HttpResponseRedirect('/')
    else:
        fm=Registration()
    return render(request,'student/home.html',{'f':fm}) 
