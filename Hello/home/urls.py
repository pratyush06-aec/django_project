# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('lists/', views.lists, name='lists'),
    path('arrivals/', views.arrivals, name='arrivals'),
    path("cart/", views.cart, name="cart"),
    path("add-to-cart/", views.add_to_cart, name="add_to_cart"),
]
