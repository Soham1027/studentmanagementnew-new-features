from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import STAaccounts,Staff
from django.contrib import messages

#hod
@login_required(login_url="/")
def hod_home(request):
    return render(request,'hod/hod_home.html')    
@login_required(login_url="/")
def add_staff(request):
    if request.method =="POST":
       username=request.POST.get('username')
       email=request.POST.get('email')
       password=request.POST.get('password')
       gender=request.POST.get('gender')
       
       if STAaccounts.objects.filter(email=email).exists():
           messages.warning(request,'Email already taken')  
           return redirect('addstaff')
       if STAaccounts.objects.filter(username=username).exists():
           messages.warning(request,'username already taken')  
           return redirect('addstaff')
       else:
           user=STAaccounts(username=username,email=email,p_type=2)
           user.set_password(password)
           user.save()
           
           staff=Staff(
               admin=user,
               gender=gender,
           )
           staff.save()
           messages.success(request,'staff are successfully add')
           return redirect('addstaff')
    return render(request,'hod/add_staff.html')    
@login_required(login_url="/")
def view_staff_admin(request):
    staff=Staff.objects.all()
    context={
        'staff':staff,
        
    }
    return render(request,'hod/view_staff_admin.html',context)   

@login_required(login_url="/")
def view_staff(request):
    staff=Staff.objects.all()
    context={
        'staff':staff,
        
    }
    return render(request,'hod/view_staff.html',context)   
@login_required(login_url="/")
def edit_staff(request,id):
    staff=Staff.objects.filter(id=id)
    context={
        'staff':staff,
               
        
    }
    return render(request,'hod/staff_edit.html',context)   
@login_required(login_url="/")
def update_staff(request):
    if request.method =="POST":
        staff_id=request.POST.get('staff_id')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        gender=request.POST.get('gender')
        
        user=STAaccounts.objects.get(id=staff_id)
        user.username=username
        user.email=email
        if password != None and password != "":
            user.set_password(password)
        user.save()
        
        staff=Staff.objects.get(admin=staff_id)
        staff.gender=gender
        
        staff.save()
        messages.success(request,'staff is successfully updated')
        return redirect('viewstaff')
       
            
    return render(request,'hod/staff_edit.html')   
@login_required(login_url="/")
def delete_staff(request,admin):
   staff=STAaccounts.objects.get(id=admin)
   staff.delete()
   messages.success(request,'records are successfully deleted')
   return redirect('viewstaff')
