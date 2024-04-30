from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
#hod
@login_required(login_url="/")
def student_home(request):
      return render(request,'student/student_home.html')
@login_required(login_url="/")
def add_subject(request):
    return render(request,'student/add_subject.html')
@login_required(login_url="/")
def mainsubject(request):
    subject_name=request.POST.get('subject_name')
    return render(request,'student/student.html')
