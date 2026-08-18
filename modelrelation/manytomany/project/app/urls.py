from django.urls import path
from . import views

urlpatterns = [

    path('', views.landing, name='landing'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('add-course/', views.add_course, name='add_course'),

    path('add-student/', views.add_student, name='add_student'),

    path('view-student/', views.view_student, name='view_student'),

]