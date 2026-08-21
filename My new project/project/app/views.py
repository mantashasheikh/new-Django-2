from django.shortcuts import render,redirect
from .models import Student
from .models import ExamForm
from django.views.decorators.cache import never_cache
from django.contrib import messages
import random

# Create your views here.
def landing(req):
    return render(req,'home.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')

@never_cache
def register(req):
    if req.method == "POST":
        n = req.POST.get('name')
        e = req.POST.get('email')
        c = req.POST.get('city')
        p = req.POST.get('password')
        cp = req.POST.get('con_password')
        i = req.FILES.get('image')  
        r = req.FILES.get('resume')
        g = req.POST.get('gender')
        q = req.POST.get('qualification')
        d = req.POST.get('description')
        # print(n,e,c,i,r,g,q,d)
        user = Student.objects.filter(email=e)
        if user:
            msg = "User already exist"
            return render(req,'register.html',{'msg':msg,'register':True})
        else:
            if p == cp:
                Student.objects.create(name=n,email=e,city=c,image=i,resume=r,password=p,gender=g,qualification=q,description=d)
                msg = "Registration Done........"
                return render(req,'login.html',{'msg':msg,'login':True})
            else:
                msg = "Password and Conform+password not matched....."
                return render(req,'register.html',{'msg':msg,'register':True})
    return render(req,'register.html',{'register':True})

@never_cache
def login(req):
    if req.method == 'POST':
        e = req.POST.get('email')
        p = req.POST.get('password')

        user =  Student.objects.filter(email=e)
        if not user:
            msg = "Email id is not register... Please register first..!!!!!!"
            return render(req,'login.html',{'login':True,'msg':msg})
        else:
            user_data =  Student.objects.get(email=e)
            db_user_pass = user_data.password 
            if db_user_pass == p :
                req.session['user_id'] = user_data.id
                return redirect("dashboard")
    return render(req,'login.html')


@never_cache
def dashboard(req):
    if 'user_id' in req.session :
        user_data = Student.objects.get(id=req.session.get('user_id'))
        return render(req,'dashboard.html',{'data':user_data})
    msg = "Please login first"
    return render(req,'dashboard.html',{'login':True,'msg':msg})


@never_cache
def dashboard_home(req):
    return render(req , "dashboard_home.html")

def profile(req):
    return render(req , 'profile.html')



def fill_exam_form(req):
    if 'user_id' in req.session :
        if req.method == "POST":
            fn = req.POST.get('firstName')
            ln = req.POST.get('lastName')
            e = req.POST.get('email')
            m = req.POST.get('mobile')
            dob = req.POST.get('dob')
            g = req.POST.get('gender')
            a = req.POST.get('address')
            ex = req.POST.get('exam')
            print(ex)
            c = req.POST.get('center')
            p = req.FILES.get('photo')
            f = req.FILES.get('file')
            check_subject = ExamForm.objects.filter(exam=ex)
            if not check_subject :
                 
                ExamForm.objects.create(first_name=fn,last_name=ln,email=e,mobile=m,dob=dob,
                                    gender=g,address=a,exam=ex,exam_center=c,photograph=p,signature=f)
            
                user_data = Student.objects.get(id=req.session.get('user_id'))
                msg = "Exam form submited succesfully"
                return render(req,'fill_exam_form.html',{'data':user_data, 'exam_form':True , 'msg':msg})
            else:
                msg = "Exam form already submited"
                user_data = Student.objects.get(id=req.session.get('user_id'))
                return render(req,'fill_exam_form.html',{'data':user_data, 'exam_form':True , 'msg':msg})
        else:
            user_data = Student.objects.get(id=req.session.get('user_id'))
            return render(req,'fill_exam_form.html',{'data':user_data, 'exam_form':True})
    return redirect('login')
   

def show_details(req):
    if 'user_id' in req.session:
        Exam_data = ExamForm.objects.all()
        user_data = Student.objects.get(id=req.session.get('user_id'))
        return render(req,  'show_details.html' , {'Exam_data':Exam_data , 'data':user_data})
    return redirect('login')

def search(req):
    if req.method == "POST":
        xyz = req.POST.get("search")
        ser_data = Student.objects.filter(name__icontains=xyz)
        return render(req, 'show_details.html')    

def edit(req,pk):
    if 'user_id' in req.session:
        user_data = Student.objects.get(id=req.session.get('user_id'))
        exam_data = ExamForm.objects.get(id=pk)
        return render(req,'fill_exam_form.html',{'data':user_data, 'exam_form':True , 'Exam_data':exam_data})

def updateform(req,pk):
    if 'user_id' in req.session:
        if req.method=="POST":
            Exam_data = ExamForm.objects.get(id=pk)
            fn = req.POST.get('firstName')
            ln = req.POST.get('lastName')
            e = req.POST.get('email')
            m = req.POST.get('mobile')
            dob = req.POST.get('dob')
            g = req.POST.get('gender')
            a = req.POST.get('address')
            ex = req.POST.get('exam')
            c = req.POST.get('center')
            p = req.FILES.get('photo')
            print(p)
            f = req.FILES.get('file')
            Exam_data.first_name = fn
            Exam_data.last_name = ln
            Exam_data.email = e
            Exam_data.mobile = m
            Exam_data.dob = dob
            Exam_data.gender = g
            Exam_data.address = a
            Exam_data.exam = ex
            Exam_data.exam_center = c
            if p is not None:
                Exam_data.photograph = p

            if f is not None:
                Exam_data.signature = f
            Exam_data.save()
            Exam_data = ExamForm.objects.all()
            print(Exam_data)
            user_data = Student.objects.get(id=req.session.get('user_id'))
            return render(req,  'show_details.html' , {'Exam_data':Exam_data , 'data':user_data})


def delete(req,pk):
    if 'user_id' in req.session:
        ExamForm.objects.get(id=pk).delete()
        Exam_data = ExamForm.objects.all()
        user_data = Student.objects.get(id=req.session.get('user_id'))
        return render(req,  'show_details.html' , {'Exam_data':Exam_data , 'data':user_data})
    return redirect('login')


        


def logout(req):
    if  'email' in req.session and 'password' in req.session :
        print(req.session)
        req.session.flush()
        # user=Session.objects.all()
        # print(user)
        # user.delete()
        return redirect('login')
    return redirect('login')


# flow of forget password

from django.core.mail import send_mail
# from project.settings import EMAIL_HOST_USER

# def mail_service(req):
#     send_mail(
#       "Test mail",
#       "This is test message from django server",
#     #   "neeraj.patel2505@gmail.com",
#       "EMAIL_HOST_USER",
#       ["nkurmbanshi@gmail.com"],
#       fail_silently=False,
# )   
    

def forget_password(req):
    return render(req, "forgot_password.html")


def send_otp(req):
    if req.method == "POST":
        e = req.POST.get("email")

        user = Student.objects.filter(email=e)

        if not user:
            messages.warning(req, "Email Id Not Registered")
            return redirect("forget_password")

        otp = random.randint(11111, 99999)

        send_mail(
            "Otp",
            f"your otp from django server is {otp}",
            "neeraj.patel2505@gmail.com",
            [e],
            fail_silently=False,
        )

        req.session["email"] = e
        req.session["otp"] = otp

        return redirect("submit_otp")

    return render(req, "forget_password.html")

def varify_otp(req):
    if req.method == "POST":
        sub_otp = req.POST.get("sub_otp")
        session_otp = req.session.get("otp")

        if str(sub_otp) != str(session_otp):
            messages.warning(req, "Please enter valid OTP")
            return redirect("submit_otp")
        else:
            return redirect("reset_password")

    return render(req, "submit_otp.html")


def reset(req):
    if req.method == "POST":
        np = req.POST.get("new_password")
        cnp = req.POST.get("con_new_password")

        if np != cnp:
            messages.warning(
                req,
                "New password & confirm new password not matched"
            )
            return redirect("reset_password")

        e = req.session.get("email")

        old_data = Student.objects.get(email=e)
        old_data.password = np
        old_data.save()

        return redirect("login")

    return render(req, "reset_password.html")