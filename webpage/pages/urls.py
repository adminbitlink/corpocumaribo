from django.urls import path
from . import views
app_name = 'pages'
urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('about-us/', views.about_us, name='about_us'),
]