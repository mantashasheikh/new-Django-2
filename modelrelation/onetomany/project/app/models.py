from django.db import models

# Create your models here.

class Department(models.Model):
	d_name = models.CharField(max_length=50)
	d_disc = models.TextField()
	
	def __str__(self):
		return self.d_name        


class Student(models.Model):
	s_name = models.CharField(max_length = 20)
	s_city = models.CharField(max_length = 20)
	dep_name = models.ForeignKey( Department, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.s_name
