from django.shortcuts import render
from .models import Student

# Create your views here.
def landing(req):
    # Student.objects.create(name="Mantasha",email="man@gmail.com",city="Bhopal")
    # Student.objects.bulk_create([Student(name="Arav",email="arav@gmail.com",city="Delhi"),
    #                              Student(name="gaurav",email="g@gmail.com",city="Mumbai"),
    #                              Student(name="meena",email="meena@gmail.com",city="jaipur")])
    
    # data = Student.objects.earliest('name')
    # print('Earliest : ', data)
    # data = Student.objects.latest('name')
    # print('Latest : ', data)
    
    # data = Student.objects.earliest('city')
    # print('Earliest_city : ', data)
    # data = Student.objects.latest('city')
    # print('Latest_city : ', data)
    
    # data = Student.objects.first()
    # print('first : ',data)
    # data = Student.objects.last('name')
    # print('lastest : ',data)
    # data = Student.objects.get()
    # print('lastest : ',data)
    
    # data = Student.objects.filter(name = "Arav")
    # print('Earliest : ', data)
    
    # data = Student.objects.all()
    # print('Earliest : ', data)
    
    # data = Student.objects.exclude(name = "Arav")
    # data = Student.objects.values()
    # data = Student.objects.values_list()
    # data = Student.objects.values('name' , 'city)
    # data = Student.objects.values_list('name' , 'city)
    print(data)
    
    
    
    
    
    
    
    
    
    
    
    
    
    return render(req, 'landing.html')
