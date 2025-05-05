from django.shortcuts import render

# Create your views here.
def home(r):
    return render(r, 'student/home.html')
def profile(r,my_id):
    dic={"id":my_id,}
    return render(r, 'student/profile.html',dic)
