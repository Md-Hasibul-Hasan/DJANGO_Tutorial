from django.shortcuts import render
from table.models import Info

# Create your views here.

def info(req):
    t=Info.objects.all()
    data={ "key" : t}
    return render(req, 'table/table.html', data)