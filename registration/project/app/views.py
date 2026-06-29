from django.shortcuts import render,redirect

# Create your views here.
def landing(req):
    render(req, 'landing.html')
    
def register(req):
    if req.method == 'POST':
        n = req.POST.get('fullname')
        e = req.POST.get('email')
        p = req.POST.get('phone')
        cn = req.POST.get('college')
        b = req.POST.get('branch')
        y = req.POST.get('year')
        cgpa = req.POST.get('cgpa')
        skills = req.POST.get('skills')
       
        return redirect('register')
    return render(req, 'landing.html')
