from django.shortcuts import render,HttpResponse,redirect
from blog.models import Post, Blogpost
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def bloghome(request):
    all_post = Post.objects.all()
    context={
        "all_post":all_post
    }
    print("hariom")
    return render(request,'blog/bloghome.html',context)
#def blogpost(request):

 #   all_post=Post.objects.all()
  #  context={
   #     "all_post":all_post
    #}
    #return render(request,'blog/blogpost.html',context)    
def blogdetail(request,id):
    obj=Post.objects.get(id=id)
    if request.method=='POST':
        comment = request.POST['comment']
        user = request.user
        c = Blogpost(comments=comment,post=obj,user=user)
        c.save()
        messages.success(request,"your comment is posted")
        all = Blogpost.objects.filter(post=obj)
        context={
            'detail':obj,
            'all': all
            }
        return render(request,'blog/blogdetail.html',context)       
    else:
        all = Blogpost.objects.filter(post=obj)
        context={
            'detail':obj,
            'all': all
            }
        return render(request,'blog/blogdetail.html',context)
def bloglogin(request):
        print('hello')
        title=request.POST['title']
        content=request.POST['content']
        user = request.user
        c=Post(title=title,content=content,user=user)
        c.save()
        messages.success(request,'your content is posted')
        return redirect('bloghome')
def search(request):
    query=request.GET['query']
    obj=Post.objects.filter(title__contains=query)   
    context={
        'all':obj
    }
    return render(request,'blog/search.html',context)

def profile(request,id):
    profile = User.objects.get(id=id)
    post = Post.objects.filter(user=profile)
    context = {
        'profile':profile,
        'post':post
    }
    print(post)
    return render(request,'blog/profile.html',context)






    

