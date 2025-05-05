from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('info/', views.info, name='info'),
    path('update/<x>/', views.update, name='update'),
    path('delete/<x>/', views.delete, name='delete'),
    path("login/", views.login, name="login"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.logout, name="logout"),
]