from django.shortcuts import render

# Create your views here.

def learndj(request):
    data={
        "data1":{
            "key1":"hasib",
            "key2":23,
            
        },
        "data2":{
            "key1":"asif",
            "key2":23,
            
        },
        "data3":{
            "key1":"rohan",
            "key2":23,
            
        },
    }
    
    info={"key":data}
    return render(request,"./course/index.html",info)