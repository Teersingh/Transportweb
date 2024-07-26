from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/',views.index,name='index'),   
    path('contact/',views.contact,name='contact'),
    path('service/',views.service,name='service'),
    path('gallery/',views.shop,name='shop'),
    path('company/',views.company,name='company'),
    path('about/',views.about,name='about'),
    path('<slug:city>/',views.get_city,name='city')
]