from django.shortcuts import render
from .models import *

# Create your views here.
def landing(req):
    return render(req, 'landing.html')

def set_session(req):
    if req.method=='POST':
        n = req.POST.get('name')
        e = req.POST.get('email')
        a = req.POST.get('age')
        req.session['name'] = n
        req.session['email'] =e
        req.session['age'] = a
            
        return render(req,'landing.html',{'msg':"Data set successfully in session"})
    
    return render(req ,'landing.html', {'set': True} )
    


def get_session(req):
    if 'name' in req.session and 'email' in req.session and 'age' in req.session :
        n = req.session.get('name')
        e = req.session.get('email')
        a = req.session.get('age')
       
        data = {
            'name':n,
            'email':e,
            'age':a,
        }
        return render(req,'landing.html',{'data':data , 'msg':"data get successfully......"})
    
    

def del_session(req):
    # del req.session['name'] 
    # del req.session['email'] 
    # del req.session['age']
    
    # req.session.clear()
    
    req.session.flush()
    return render(req, 'landing.html', {'msg1': 'session deleted succesfully'}) 

       
