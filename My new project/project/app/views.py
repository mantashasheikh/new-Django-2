from django.shortcuts import render,redirect
from .models import Student
from .models import ExamForm

# Create your views here.
def landing(req):
    return render(req,'home.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')

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

def dashboard(req):
    if 'user_id' in req.session :
        user_data = Student.objects.get(id=req.session.get('user_id'))
        return render(req,'dashboard.html',{'data':user_data})
    msg = "Please login first"
    return render(req,'dashboard.html',{'login':True,'msg':msg})

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
    return render(req , 'login')

def edit(req,pk):
    if 'user_id' in req.session:
        user_data = Student.objects.get(id=req.session.get('user_id'))
        exam_data = ExamForm.objects.get(id=pk)
        return render(req,'fill_exam_form.html',{'data':user_data, 'exam_form':True , 'Exam_data':exam_data})
        

def logout(req):
    return redirect('login')


   
    
