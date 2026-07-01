from django.shortcuts import render,redirect

# Create your views here.
def landing(req):
    return render (req, 'landing.html')
    
def register(req):
    if req.method == 'POST':
        req.session['name'] = req.POST.get('fullname')
        req.session['email'] =req.POST.get('email')
        req.session['phone'] = req.POST.get('phone')
        req.session['college'] = req.POST.get('college')
        req.session['branch'] = req.POST.get('branch')
        req.session['year'] =  req.POST.get('year')
        req.session['cgpa'] =  req.POST.get('cgpa')
        req.session['skills'] = req.POST.get('skills')
        
       
        return redirect('login')
    return render(req, 'landing.html', {'register':True})

def login(req):
    if req.method == "POST":
        e = req.POST.get('email')
        
        ph = req.POST.get('phone')
        # e1 = req.session['email']
        e1 = req.session.get('email')
        
        # ph1 = req.session['phone']
        ph1 = req.session.get('phone')
        # print(e,e1)
        # print(ph,ph1)
        if e==e1 and ph==ph1:
            return redirect('dashboard')
        else:
            return render(req , 'landing.html', {'login':True, 'msg':"email and phone number not match with session"})
    return render(req , 'landing.html', {'login':True})   
   

def dashboard(req):
    data =  {'name':req.session.get('name'),
             'email':req.session.get('email'),
             'phone':req.session.get('phone'),
             'college':req.session.get('college'),
             'branch':req.session.get('branch'),
             'year':req.session.get('year'),
             'cgpa':req.session.get('cgpa'),
             'skills':req.session.get('skills')
            } 
    return render(req , 'dashboard.html', {'data':data})    
            
        
   
def logout(req):
    if 'email' in req.session and 'phone' in req.session:
        req.session.flush()
        
    return redirect('register')    