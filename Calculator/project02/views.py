from django.shortcuts import render,redirect
from django.http import HttpResponse
from modelname.models import modelclass
from django.core.paginator import Paginator
from FORM.models import formclass



def Home(request):

    Ans=0
    data={}
    try:
        # if request.method=="GET":
        #     n1=request.GET.get("num1")
        #     n2=request.GET.get("num2")

        if request.method=="POST":
            n1=request.POST.get("num1") 
            n2=request.POST.get("num2")
            n1=int(n1)
            n2=int(n2)
            print(n1+n2)
            Ans=n1+n2
            data={
                "first":n1,
                "second":n2,
                "sum":Ans
            }
            
            # url="/about/?show={}".format(Ans)
            # return redirect(url)
    except:
        pass
    
    return render(request, "home.html",data)

def About(request):
    if request.method=="GET":
        value=request.GET.get("show")
    return render(request, "about.html",{"key":value})

def Contuct(request):
    modeldata=modelclass.objects.all()
    paginator=Paginator(modeldata,1)
    page_number=request.GET.get("page")
    page_obj=paginator.get_page(page_number)

    if request.method=="GET":
        st=request.GET.get("filter")
        if st!=None:
            modeldata=modelclass.objects.filter(icon__icontains=st)
    data={
        "k":page_obj,
    }
    return render(request, "contuct.html",data)


def Help(request):

    result=""
    data={}
    try:
        if request.method=="POST":
            n1=int(request.POST.get("num1"))
            n2=int(request.POST.get("num2"))
            operator=request.POST.get("opr")
            if operator=="+":
                result=n1+n2
            elif operator=="-":
                result=n1-n2
            elif operator=="*":
                result=n1*n2
            else:
                result=n1/n2
            data={
                "key1":n1,
                "key2":n2,
                "key3":result,
            }
            

            

    except:
        result="invalid"

    return render(request, "help.html",data)


def Submit(request):
    Ans=0
    data={}
    try:
        if request.method=="POST":
            n1=request.POST.get("num1") 
            n2=request.POST.get("num2")
            n1=int(n1)
            n2=int(n2)
            print(n1+n2)
            Ans=n1+n2
            data={
                "first":n1,
                "second":n2,
                "sum":Ans
            }

            return HttpResponse(Ans)
    except:
        pass
  


def Form(request):
    dis=""
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("number")
        website=request.POST.get("web")
        message=request.POST.get("mess")
        data=formclass(name=name,email=email,phone=phone,website=website,message=message)
        data.save()
        dis="data send"


    return render(request,"form.html",{"key":dis})