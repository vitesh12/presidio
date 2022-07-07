from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.views.generic import ListView
from .models import Member 
class MemberList(ListView):
    model = Member

def index(request):
    return render(request,'index.html')
    #return HttpResponse("helllo")
def login(request):
    if request.method == 'POST':
        name = request.POST['uname']
        login.name=name
        password = request.POST['psw']
        tp = request.POST.get('user')
        user = auth.authenticate(username=name,password=password)
        if user is not None:
            auth.login(request,user)
            if tp == 'Tutor':
                return redirect('tutor')
            elif tp == 'Student':
                return redirect('studentview')   
            else:
                return redirect('index')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        psw = request.POST['psw']
        c_psw = request.POST['psw-repeat']
        if psw == c_psw:
            user = User.objects.create_user(username=name,password=psw,email=email)
            user.save();
            return redirect('login')
        else:
            return redirect('register')
    else:
        return render(request,'register.html')
def tutor(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        qua = request.POST['qua']
        gender = request.POST['gender']
        subject = request.POST['subject']
        en=Member(firstname=firstname,qua=qua,gender=gender,subject=subject)
        en.save()
        data=Member.objects.all()
        data1={
            'data':data
        }
        return render(request,'tutorview.html',data1)
    else:
        return render(request,'tutor.html')

def studentview(request):
    data=Member.objects.all()
    data1={
            'data':data
        }
    return render(request,'studentview.html',data1)

def student_details(request):
    return render(request,'student_details.html',{'n':login.name})

def send_mail(request):
    if request.method == 'POST':
        email = request.POST['mail']
        messages = request.post['mes']
        print(email)
    else:
        return render(request,'student_details.html')

def signout(request):
    return render(request,'index.html')

def tutorview(request):
    data=Member.objects.all()
    data1={
            'data':data
        }
    return render(request,'tutorview.html',data1)