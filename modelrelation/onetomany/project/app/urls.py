from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('add-department/', views.department_view, name='department_view'),
    path('add-student/', views.student_view, name='student_view'),
    path('forward-access/', views.forward_access, name='forward_access'),
    path('backward-access/', views.backward_access, name='backward_access'),
]