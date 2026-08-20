from django.shortcuts import render, redirect
from .models import RollNo, Student


def landing(req):
    return render(req, 'landing.html')


def roll_number_view(req):

    if req.method == "POST":

        roll_no = req.POST.get("roll_no")

        if roll_no:
            RollNo.objects.create(
                roll_no=roll_no
            )

            return redirect('student_view')

    return render(req, 'landing.html', {'show_roll_form': True})


def student_view(req):

    roll_numbers = RollNo.objects.all()

    if req.method == "POST":

        Student.objects.create(
            name=req.POST.get("name"),
            email=req.POST.get("email"),
            city=req.POST.get("city"),
            address=req.POST.get("address"),
            contact=req.POST.get("contact"),
            roll_id=req.POST.get("roll")
        )

        return redirect('landing')

    return render(req, 'landing.html', {'show_student_form': True, 'roll_numbers': roll_numbers})

from django.core.mail import send_mail
from project.settings import EMAIL_HOST_USER

def mail_service(req):
    send_mail(
      "Test mail",
      "This is test message from django server",
    #   "neeraj.patel2505@gmail.com",
      "EMAIL_HOST_USER",
      ["nkurmbanshi@gmail.com"],
      fail_silently=False,
)

