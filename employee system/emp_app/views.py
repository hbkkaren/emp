from django.shortcuts import render,HttpResponse
from .models import Role,Department,Empoyee,User
from datetime import  datetime
from django.db.models import Q



def main_index(request):
    return render(request,'main_index.html')


def signup(request):
	if request.method=="POST":
		try:
			User.objects.get(email=request.POST['email'])
			msg="Email Already Regsistered"
			return render(request,'signup.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
						fname=request.POST['fname'],
						lname=request.POST['lname'],
						email=request.POST['email'],
						mobile=request.POST['mobile'],
						address=request.POST['address'],
						gender=request.POST['gender'],
						password=request.POST['password'],
						
					)
				msg="User Sign Up Successfully"
				return render(request,'signup.html',{'msg':msg})
			else:
				msg="Password & Confrim Password Does Not Matched"
				return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'signup.html')

def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			if user.password==request.POST['password']:
				request.session['email']=user.email
				request.session['fname']=user.fname
				return render(request,'index.html')
			else:
				msg="Incorrect Password"
				return render(request,'login.html',{'msg':msg})
		except:
			msg="Email Not Regsistered"
			return render(request,'login.html',{'msg':msg})
	else:
		return render(request,'login.html')




def index(request):
    return render(request,"index.html")


def all_emp(request):
    emps = Empoyee.objects.all()
    context = {
        'emps':emps
    }
    print(context)
    return render(request,"all_emp.html",context)

def add_emp(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = request.POST['salary']
        bonus = request.POST['bonus']
        phone = request.POST['phone']
        dept = request.POST['dept']
        role = request.POST['role']
        new_emp = Empoyee(first_name = first_name,last_name= last_name,salary=salary,phone = phone,dept_id = dept ,role_id = role, hire_date = datetime.now())
        new_emp.save()
        return HttpResponse('employee added successfully')
    
    elif request.method==  "GET":
        return render(request,'add_emp.html')

    else :
        return HttpResponse('An exception occurs !  employee')   
        
        
        


    return render(request,"add_emp.html")

def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Empoyee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid EMP ID")
    emps = Empoyee.objects.all()

   
    
    return render(request, 'remove_emp.html',{'emps':emps})


def filter_emp(request):
    if request.method == "POST":
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Empoyee.objects.all()

        if name: 
            emps = emps.filter(Q(first_name__icontains = name)| Q(last_name__icontains = name))
        
        if dept: 
            emps = emps.filter(dept__name = dept)
        
        if role: 
            emps = emps.filter(role__name = role)

        context = {
            'emps': emps
        }
        return render(request, 'all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')

    return render(request,'filter_emp.html')
