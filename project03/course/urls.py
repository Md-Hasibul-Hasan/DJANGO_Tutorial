from django.urls import path
from . import views

urlpatterns = [
        path('learn/', views.learn),
        path('c1/', views.dyna),
]
