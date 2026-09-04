from django.db import models


class Student(models.Model):
    stu_name = models.CharField(max_length=100)
    stu_email = models.EmailField(unique=True)
    stu_city = models.CharField(max_length=100)
    stu_add = models.TextField()

    def _str_(self):
        return self.stu_name
