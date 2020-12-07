from django.urls import path
from .import views


urlpatterns = [
    path("", views.home, name='home'),
    path('password/', views.mypassword_info, name="password")


]
