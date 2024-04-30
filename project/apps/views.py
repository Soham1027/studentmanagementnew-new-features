from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from apps.models import STAaccounts
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth import authenticate,login,logout

from apps.EmailBackEnd import EmailBackEnd

# Create your views here.
def LOGIN(request):
    return render(request, 'login.html')
 
def doLogin(request):
    #form =loginform(request.POST or None)
 
    if request.method=="POST":
        user= EmailBackEnd.authenticate(request,
                                        username=request.POST.get('username'),
                                        password=request.POST.get('password'),)
                                     
           
        if user is not None:
            login(request, user)
            p_type=user.p_type
            if p_type=='1':
               return redirect('hod_home')
            elif p_type=='2':
                return redirect('staff_home')


            elif p_type=='3':
               return redirect('student_home')


            else:
                messages.error(request,'email and password incorrect')
                return redirect("login")

        else:
            messages.error(request,'email and password incorrect')
            return redirect("login")
            
def BASE(request):
    return render(request,'extends/basemain.html')
def Logoutpage(request):
    logout(request)
    return redirect('login')
def profile(request):
    user=STAaccounts.objects.get(id=request.user.id)
    context={
         "user":user,
         
     }
    return render(request,'profile.html',context)
def profileupdate(request):
    if request.method == "POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(username,email,password)
        try:
            customuser=STAaccounts.objects.get(id=request.user.id)
            customuser.username=username
            customuser.email=email
            if password != None and password != "":
                  customuser.set_password(password)
            customuser.save()
            messages.success(request,"your profile updated")
            redirect('profile')
          
                
            
        except:
            messages.error(request,"failed to update")
        
        
    return render(request,'profile.html')

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/change_password.html'
    post_reset_login = True
    success_url = reverse_lazy('any-login-url') 