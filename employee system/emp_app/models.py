from django.db import models

# Create your models here.



class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.PositiveIntegerField()
	address=models.TextField()
	gender=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	

	def __str__(self):
		return self.fname+" "+self.lname


class Department(models.Model):
    name = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100,null=False)
    def __str__(self) -> str:
        return self.name



class Empoyee(models.Model):
    first_name = models.CharField(max_length=100,null=False)
    last_name  = models.CharField(max_length=100)
    dept = models.ForeignKey(Department,on_delete = models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()

    def __str__(self) -> str:
        return "%s %s %s" %(self.first_name,self.last_name,self.phone)