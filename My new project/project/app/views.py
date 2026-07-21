from django.shortcuts import render
from .models import Student

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
   return render(req,'login.html')

def dashboard(req):
    return render(req,'dashboard.html')
    
