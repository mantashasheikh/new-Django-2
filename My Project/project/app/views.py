from django.shortcuts import render,redirect
from .models import Empolyee

# Create your views here.
def landing(req):
    return render(req,'home.html')

def base(request):
    return render(request, 'base.html')

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
        user = Empolyee.objects.filter(email=e)
        if user:
            msg = "User already exist"
            return render(req,'register.html',{'msg':msg,'register':True})
        else:
            if p == cp:
                Empolyee.objects.create(name=n,email=e,city=c,image=i,resume=r,password=p,gender=g,qualification=q,description=d)
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

        user =  Empolyee.objects.filter(email=e)
        if not user:
            msg = "Email id is not register... Please register first..!!!!!!"
            return render(req,'login.html',{'login':True,'msg':msg})
        else:
            user_data =  Empolyee.objects.get(email=e)
            db_user_pass = user_data.password 
            if db_user_pass == p :
                req.session['user_id'] = user_data.id
                return redirect("dashboard")
    return render(req,'login.html',{'login':True})

def dashboard(req):
    if 'user_id' in req.session :
        user_data = Empolyee.objects.get(id=req.session.get('user_id'))
        return render(req,'dashboard.html',{'data':user_data})
    msg = "Please login first"
    return render(req,'login.html',{'login':True,'msg':msg})


def logout(req):
    if 'email' in req.session and 'password' in req.session :
        req.session.flush()
        return redirect('login')
    return redirect('login')
