from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dynamicurlhomepage(request):
    return render(request,"show.html")

def page(request,id=1):  
    if id ==1:
        data={      
            "my_id":id,
            "name":"hasib",
        }
    elif id ==2:
        data={      
            "my_id":id,
            "name":"asif",
        }
    elif id ==3:
        data={      
            "my_id":id,
            "name":"ramim",
        }

    return render(request,"page.html",data)

