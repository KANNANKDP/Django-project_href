from django.urls import path
from . import views

urlpatterns = [
    path('',views.homePageView,name="home"),
    path('welcome/',views.welcomePageView,name="welcome"),
    path('about/',views.aboutPageView,name="about"),
]