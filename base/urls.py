from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_page, name="home"),
    path('about/', views.about_page, name="about"),
    path('about/technologies/', views.about_technologies_page, name='technologies'),
    path('about/dev/', views.about_dev_page, name='dev'),
    path('work/', views.work_page, name="work"),
    path('projects/', views.projects_page, name="projects"),
    path('contact/', views.contact_page, name="contact"),
]