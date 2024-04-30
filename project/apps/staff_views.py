from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import STAaccounts,Student,timetable
from django.contrib import messages
from .forms import addtt
#staff
@login_required(login_url="/")
def staff_home(request):
    return render(request,'staff/staff_home.html')    
@login_required(login_url="/")
def add_student(request):
    if request.method == "POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        gender=request.POST.get('gender')
        if STAaccounts.objects.filter(email=email).exists():
            messages.warning(request,'Email already taken')   
            return redirect('addstudent')
        if STAaccounts.objects.filter(username=username).exists():
            messages.warning(request,'Username already taken')   
            return redirect('addstudent')
        else:
            user=STAaccounts(
                username=username,
                email=email,
                p_type=3
            )
            user.set_password(password)
            user.save()
            
            
            student=Student(
                admin=user,
                gender=gender,
                
            )
            student.save()
            messages.success(request,user.username +" "+'are successfully added')
            return redirect('addstudent')
    return render(request,'staff/add_student.html')   
       
          
@login_required(login_url="/")  
def student_list_admin(request):
    student=Student.objects.all()
    context={
        'student':student,
        
    }
    return render(request,'staff/student_list_admin.html',context)   

@login_required(login_url="/")
def student_list(request):
    student=Student.objects.all()
    context={
        'student':student,
        
    }
    return render(request,'staff/student_list.html',context)   
@login_required(login_url="/")   
def student_edit(request,id):
    student=Student.objects.filter(id=id)
    context={
        'student':student,
               
        
    }
    return render(request,'staff/student_edit.html',context)   
@login_required(login_url="/")
def studentupdate(request):
    if request.method == "POST":
        student_id=request.POST.get('student_id')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        gender=request.POST.get('gender')
        
        user=STAaccounts.objects.get(id=student_id)
        user.username=username
        user.email=email
        if password != None and password != "":
            user.set_password(password)
        user.save()
        
        student=Student.objects.get(admin=student_id)  
        student.gender=gender
        
        
        student.save()
        messages.success(request,'Record are successfully updated')
        return redirect('student_list')
  
   
    return render(request,'staff/student_edit.html')   
@login_required(login_url="/")
def studentdelete(request,admin):
    student=STAaccounts.objects.get(id=admin)
    student.delete()
    messages.success(request,'record are successfully deleted')
    return redirect('student_list')
@login_required(login_url="/")
def add_timetable(request,id=0):
        if request.method =="GET":
            if id==0:
                
              form=addtt()
            else:
                tt=timetable.objects.get(pk=id)
                form=addtt(instance=tt)
            return render(request,'staff/timetable/addtimetable.html',{'form':form})
        else:
            if id==0:
                
                form=addtt(request.POST)
            else:
                tt=timetable.objects.get(pk=id)
                form=addtt(request.POST,instance=tt)
            if form.is_valid():
              form.save() 
            return redirect('staff_home')
@login_required(login_url="/")  
def view_timetable(request):
    viewtt=timetable.objects.all()
    context={
        'viewtt':viewtt,
    }
    return render(request,'staff/timetable/viewtimetable.html',context)
@login_required(login_url="/")
def delete_timetable(request,id):
    tt=timetable.objects.get(pk=id)
    tt.delete()
    
    return redirect('staff_home')
@login_required(login_url="/")
def view_timetable_student(request):
    viewtt=timetable.objects.all()
    context={
        'viewtt':viewtt,
    }
    return render(request,'staff/timetable/viewtimetablestudent.html',context)