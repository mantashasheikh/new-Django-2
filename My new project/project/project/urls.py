"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name="home"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact , name='contact'),
    path('service', views.service, name='service'),
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    # path('profile/', views.profile, name='profile'),
    path('fill_exam_form/', views.fill_exam_form, name='fill_exam_form'),
    # path('show_details/', views.show_details, name='show_details'),
    path('logout/', views.logout, name='logout'),
    
    
    
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


