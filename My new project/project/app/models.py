from django.db import models

# Create your models here.
class Student(models.Model):

    CITY_CHOICES = (
        ('Bhopal', 'Bhopal'),
        ('Indore', 'Indore'),
        ('Delhi', 'Delhi'),
        ('Mumbai', 'Mumbai'),
        ('Pune', 'Pune'),
    )

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

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=20, choices=CITY_CHOICES)
    image = models.ImageField(upload_to='student_images/')
    resume = models.FileField(upload_to='student_resume/')
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    qualification = models.CharField(max_length=20, choices=QUALIFICATION_CHOICES)
    description = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name
    
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
    subject = models.CharField(max_length=30, null=True)
    photograph = models.ImageField(upload_to='photos/')
    signature = models.ImageField(upload_to='signatures/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"