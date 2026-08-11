from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('add-roll-number/', views.roll_number_view, name='roll_number_view'),
    path('add-student/', views.student_view, name='student_view'),
]