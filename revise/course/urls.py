from django.urls import path
from course import views

urlpatterns = [
path('cor/', views.course, name='course'),
]