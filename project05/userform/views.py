from django.shortcuts import render, redirect,  get_object_or_404
from .models import User
from django.contrib import messages


def user_form(request):
    # 1: collecting data from html form
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get("email")
        password = request.POST.get('password')
        confirm_password = request.POST.get('password2')
         
        if password != confirm_password:
            messages.error(request, "Passwords don't match.")
        # elif len(password) < 6:
        #     messages.error(request, "Password should be at least 6 characters.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
        else:
            # user = User(name=name, email=email, password=password)
            # user.save()
            user=User.objects.create(name=name, email=email, password=password)
            user.save()
            messages.success(request, "User information added.")
            return redirect('/userform/form')

        
    alldata={
        "data":User.objects.all(), # 3: collecting data from Database
    }
    return render(request, 'form.html', alldata)


# delete data from database from html page
def delete_data(request, id):
    dt =User.objects.get(pk=id)
    dt.delete()
    return redirect("/userform/form")


# Update and Edit
def update_data(request, id):
    user = User.objects.get(pk=id)
    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.password = request.POST.get('password')
        user.save()
        return redirect("/userform/form")

    context = {
        "id":id,
        'user': user
    }
    return render(request, 'update_info.html', context)


    
def success(request):
    return render(request, 'success.html')


# def information(request):
#     table_data=User.objects.all()
#     return render(request, "info.html", {"data":table_data})
