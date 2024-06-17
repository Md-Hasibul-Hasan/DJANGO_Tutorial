from django.http import HttpResponse
from django.shortcuts import render

def aboutUs(request):
    return HttpResponse("hello hasib")

def dynamic(request,id):
    return HttpResponse(id)

# def homepage(request):
#     return  render(request,"index.html")

# def homepage(request):

#     data={
#         "title" :"New home",

#          "pdata":"hi i am hasib",
#          "clist":["php","python","jaba"],
#          "number":[20,30,40,50],
#          "student_details":[
#              {"name": "hasib","age":43},
#              {"name":"asif","age":45}
#          ]
#     }
#     return render(request,"index.html",data)

def homepage(request):
    return  render(request,"index.html")