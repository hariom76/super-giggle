from django.shortcuts import render,HttpResponse,redirect
from blog.models import Post
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def bloghome(request):
    all_post=Post.objects.all()
    context={
        "all_post":all_post
    }
    return render(request,'blog/bloghome.html',context)
#def blogpost(request):

 #   all_post=Post.objects.all()
  #  context={
   #     "all_post":all_post
    #}
    #return render(request,'blog/blogpost.html',context)    
def blogdetail(request,id):
    obj=Post.objects.get(id=id)
    context={
        'detail':obj
    }
    return render(request,'blog/blogdetail.html',context)
def bloglogin(request):
        print('hello')
        title=request.POST['title']
        content=request.POST['content']
        author=request.POST['author']
        c=Post(title=title,content=content,author=author)
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

    

