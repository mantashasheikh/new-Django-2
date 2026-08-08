from django.db import models

class RollNo(models.Model):
    roll_no = models.IntegerField(unique=True)
    def __str__(self):
        return str(self.roll_no)

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)

    # One-to-One Relationship
    # roll = models.OneToOneField(RollNo,on_delete=models.PROTECT) # Protect to delete
    roll = models.OneToOneField(RollNo,on_delete=models.CASCADE) # Parallel delete both objects

    def __str__(self):
        return self.name
