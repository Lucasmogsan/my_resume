from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"), #tomme '' betyder den linker til home.html
    path('about.html', views.about, name="about"),
    path('resume.html', views.resume, name="resume"),
]