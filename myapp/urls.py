from django.urls import path,include
from myapp import views
urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('login_/',views.login_,name='login_'),
    path('register/',views.register,name="register"),
    path('logout_/',views.logout_,name="logout_"),
]
