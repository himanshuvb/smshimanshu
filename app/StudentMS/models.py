from django.db import models
from random import choices

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    roll = models.IntegerField(default=0)
    regno = models.IntegerField(primary_key=True)
    age = models.IntegerField(default=1,blank=True,null=True)
    div = models.IntegerField(default =0,choices=[(1,1),(2,2),(3,3),(4,4),(5,5)])
    leaves_total = models.IntegerField(default=0)
    profile = models.ImageField(default=None, null=True)
    


    def __str__(self):
        return str(self.regno)

class Leaves(models.Model):
    regno = models.ForeignKey(Student, on_delete = models.DO_NOTHING)
    name = models.CharField(max_length=200)
    reason = models.CharField(max_length=200)


    def __str__(self):
        return self.name


class Git(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.CharField(max_length=2000)

    def __str__(self):
        return self.name