from django.shortcuts import render
from .models import Student

# Create your views here.
def landing(req):
    Student.objects.create(name="Mantasha",email="man@gmail.com",city="Bhopal")
    Student.objects.bulk_create([Student(name="Arav",email="arav@gmail.com",city="Delhi"),
                                 Student(name="Mohini",email="mohi@gmail.com",city="Mumbai"),
                                 Student(name="seema",email="seema@gmail.com",city="jabalpur")])
    
    data = Student.objects.earliest('name')
    print('Earliest : ', data)
    data = Student.objects.latest('name')
    print('Latest : ', data)
    
    data = Student.objects.earliest('city')
    print('Earliest_city : ', data)
    data = Student.objects.latest('city')
    print('Latest_city : ', data)
    
    data = Student.objects.first()
    print('first : ',data)
    data = Student.objects.last('name')
    print('lastest : ',data)
    data = Student.objects.get('name':"reena")
    print('lastest : ',data)
    
    
    
    
    
    
    return render(req, 'landing.html')
