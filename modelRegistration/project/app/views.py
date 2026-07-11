from django.shortcuts import render
from .models import Register

# Create your views here.
def landing(req):
    return render(req,'landing.html')

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
        user = Register.objects.filter(email=e)
        if user:
            msg = "User already exist"
            return render(req,'landing.html',{'msg':msg,'register':True})
        else:
            if p == cp:
                Register.objects.create(name=n,email=e,city=c,image=i,resume=r,password=p,gender=g,qualification=q,description=d)
                msg = "Registration Done........"
                return render(req,'landing.html',{'msg':msg,'login':True})
            else:
                msg = "Password and Conform+password not matched....."
                return render(req,'landing.html',{'msg':msg,'register':True})
            

    return render(req,'landing.html',{'register':True})

def login(req):
    return render(req,'landing.html',{'login':True})
