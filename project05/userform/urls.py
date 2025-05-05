# userform/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.user_form, name='form'),
    path('success/', views.success, name='success'), 
    path('delete/<int:id>/', views.delete_data, name='delete'),
    path('update/<int:id>/', views.update_data, name='update'),
]
