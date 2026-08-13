from django.db import models

# Create your models here.
class Course(models.Model):
	c_name = models.CharField(max_length=10) 
	def __str__(self):
		return self.c_name

class Student2(models.Model):
	s_name = models.CharField(max_length=20)
	course = models.ManyToManyField(Course)
	def __str__(self):
		return self.s_name