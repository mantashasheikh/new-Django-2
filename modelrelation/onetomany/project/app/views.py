from django.shortcuts import render, redirect
from .models import Department, Student
from django.contrib import messages



def landing(req):
    return render(req, 'landing.html')



def department_view(req):

    if req.method == 'POST':

        d_name = req.POST.get('d_name')
        d_disc = req.POST.get('d_disc')

        department = Department.objects.filter(d_name=d_name)
        if department:
            messages.warning(req, "department name already exist")
            return redirect('department_view')
        else:

            Department.objects.create(
                d_name=d_name,
                d_disc=d_disc
            )
            messages.success(req, "department created successfully")
            return redirect('department_view')
        
    return render(req, 'landing.html', {'show_department': True})



def student_view(req):

    departments = Department.objects.all()

    if req.method == 'POST':

        s_name = req.POST.get('s_name')
        s_city = req.POST.get('s_city')
        dep_id = req.POST.get('dep_name')

        department = Department.objects.get(
            id=dep_id
        )

        Student.objects.create(
            s_name=s_name,
            s_city=s_city,
            dep_name=department
        )

        return redirect('landing')

    return render(req, 'landing.html',{'show_student': True, 'departments': departments})