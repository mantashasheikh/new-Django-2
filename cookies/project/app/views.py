from django.shortcuts import render

# Create your views here.
def landing(req):
    return render(req, 'landing.html')

def set_cookies(req):
    if req.method == "POST":
        n = req.POST.get('name')
        e = req.POST.get('email')
        a = req.POST.get('age')
        response = render(req,'landing.html',{'set_done':True})
        response.set_cookie('name',n,secure=True)
        response.set_cookie('email',e,max_age=60*60*24)
        response.set_cookie('age',a,httponly=True)
        return response
    return render(req,'landing.html',{'set':True})

def get_cookies(req):
    data = {
        'name':req.COOKIES.get('name','Guest'),
        'email':req.COOKIES.get('email','guest@gmail.com'),
        'age':req.COOKIES.get('age','0'),
        'token':req.COOKIES.get('csrftoken')
    }
    return render(req,'landing.html',{'data':data})

def del_cookies(req):
    if 'name' in req.COOKIES and 'age' in req.COOKIES and 'email' in req.COOKIES:
        response = render(req,'landing.html',{'msg':"Cookies are deleted..."})
        response.delete_cookie('name')
        response.delete_cookie('email')
        response.delete_cookie('age')
        return response

    else:
        response = render(req,'landing.html',{'msg':"Cookies are not found"})
        return response    

    
