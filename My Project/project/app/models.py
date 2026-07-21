from django.db import models

# Create your models here.
class Empolyee(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    QUALIFICATION_CHOICES = (
        ('10th', '10th'),
        ('12th', '12th'),
        ('Diploma', 'Diploma'),
        ('BCA', 'BCA'),
        ('B.Tech', 'B.Tech'),
        ('MCA', 'MCA'),
        ('M.Tech', 'M.Tech'),
        ('Other', 'Other'),
    )

    CITY_CHOICES = (
        ('Bhopal', 'Bhopal'),
        ('Indore', 'Indore'),
        ('Delhi', 'Delhi'),
        ('Mumbai', 'Mumbai'),
        ('Pune', 'Pune'),
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=50,choices=CITY_CHOICES)
    image = models.ImageField(upload_to='profile_images/')
    resume = models.FileField(upload_to='resume/')
    password = models.CharField(max_length=128)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    qualification = models.CharField(max_length=20,choices=QUALIFICATION_CHOICES)
    description = models.TextField()
    

    def __str__(self):
        return self.name



from django.db import models

class ExamForm(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.TextField()

    exam = models.CharField(max_length=20)
    exam_center = models.CharField(max_length=20)

    photograph = models.ImageField(upload_to='photos/')
    signature = models.ImageField(upload_to='signatures/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"