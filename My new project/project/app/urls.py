from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name="home"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact , name='contact'),
    path('service/', views.service, name='service'),
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('fill_exam_form/', views.fill_exam_form, name='fill_exam_form'),
    path('show_details/', views.show_details, name='show_details'),
    path('logout/', views.logout, name='logout'),
    
    
    
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

