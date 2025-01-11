from django.urls import path
from .import views

app_name = 'tasks'
urlpatterns =[
    path('',views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about')
]