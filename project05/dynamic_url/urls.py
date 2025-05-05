from django.urls import path
from . import views

urlpatterns = [
    path('d_url/',views.dynamicurlhomepage,name='dynamicurl'),
    
    path('page/<int:id>/',views.page,name='page'),
]
