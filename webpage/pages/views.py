from django.shortcuts import render

from .models import Menu, SubMenu, Noticia


def index(request):
    menus = Menu.objects.filter().order_by('id')
    submenus = SubMenu.objects.filter().order_by('id')
    noticias = Noticia.objects.filter(age__contains='2023').order_by('-id')[:3]
    return render(request, 'index.html', {'menus': menus,'submenus': submenus,'noticias': noticias})

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def about_us(request):
    return render(request, 'about-us.html')
