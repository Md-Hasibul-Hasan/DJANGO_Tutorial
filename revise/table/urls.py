from django.urls import path
from table import views

urlpatterns = [
    path('info/', views.info, name='info'),
]
