from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.index, name="Home" ),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('portfolio-details/', views.portfolio_details, name="portfolio-details"),
    path('team/', views.team, name="team"),
    path('contact/', views.contact, name="contact")

]
