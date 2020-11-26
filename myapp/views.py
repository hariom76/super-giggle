from django.shortcuts import render,HttpResponse,redirect
from myapp.models import Contact
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    if request.method=='POST':
        messages.error(request,"you have to login first")
        return redirect('login_')
    post = Post.objects.get(id=1)
    context = {
        'post':post
    }
    return render(request,'myapp/home.html',context)
def about(request):
    return render(request,'myapp/about.html') 
def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone_number=request.POST['phone_number']
        issue=request.POST['issue']
        c=Contact(name=name,email=email,phone_number=phone_number,issue=issue)
        if len(phone_number)!=10:
            messages.error(request,'contact number must contain 10 digit')
        else:    
            messages.success(request,'you record is submitted ,you will informed soon')
        c.save()    
        return redirect('/contact/')

    else:    
        return render(request,'myapp/contact.html')    

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        name1=request.POST['name1']
        name3=request.POST['name3']
        email=request.POST['email']
        phone=request.POST['phone']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if len(username)<4:
            messages.error(request,"username must be of 10 characters")
            return redirect('register')
        elif password1!=password2:
            messages.error(request,"password do not match")
            return redirect('register')
        elif User.objects.filter(username=username).exists():  
            messages.error(request,"username already taken")
            return redirect('register') 
        else:
            myuser=User.objects.create_user(username,email=email,password=password1)
            myuser.first_name=name1
            myuser.last_name=name3
            myuser.phone=phone
            myuser.save()
            messages.success(request,'your account is successfully created')
            return redirect('/')
    else:
        return render(request,'myapp/register.html')
def login_(request):
    if request.method=='POST':
        print('lol')
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'you are logged in')
            return redirect('bloghome')
        else:
            messages.error(request,'credential error')    
            return redirect('/')
    else:
        return render(request,'myapp/login.html')        
def logout_(request):
    logout(request)
    messages.success(request,"you are successfully logged out")
    return redirect('/')        