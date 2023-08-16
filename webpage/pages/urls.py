from django.urls import path
from . import views
app_name = 'pages'
urlpatterns = [
    path('', views.index, name='index'),
    path('service.html', views.service, name='service'),
    path('contact.html', views.contact, name='contact'),
    path('about.html', views.about, name='Nosotros'),
    path('blog.html', views.blog, name='blog'),
    path('single.html', views.single, name='single'),
    path('project.html', views.project, name='project'),
]