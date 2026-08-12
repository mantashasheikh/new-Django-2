from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('add-department/', views.department_view, name='department_view'),
    path('add-student/', views.student_view, name='student_view'),
]