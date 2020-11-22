from django.urls import path,include
from blog import views
urlpatterns=[
    path('',views.bloghome,name='bloghome'),
    #path('blogpost/',views.blogpost,name='blogpost'),
    path('blogdetail/<int:id>',views.blogdetail,name='blogdetail'),
    path('bloglogin/',views.bloglogin,name='bloglogin'),
    path('search/',views.search),
    #path("reply/",views.reply,name='reply')
]

