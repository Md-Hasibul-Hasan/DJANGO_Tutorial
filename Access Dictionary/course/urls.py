from django.urls import path
from course import views

urlpatterns = [
    path('page/', views.learndj,name="course"),
]
