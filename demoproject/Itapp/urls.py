from django.urls import path
from Itapp import views
from django.contrib.auth import views as v
urlpatterns=[
       path('hello/',views.hello),
       path('',views.home,name='home'),
       path('about/',views.about,name='about'),
       path('contact/',views.contact,name='contact'),
       path('register/',views.register,name='register'),
       path('login/',v.LoginView.as_view(template_name='Itapp/login.html'),name='login'),
       path('logout/',v.LogoutView.as_view(template_name='Itapp/logout.html'),name='logout'),
       path('dashboard/',views.dashboard,name='dashboard'),
       path('mailsend/',views.mailsend,name='mailsend'),
       path('profile/',views.profile,name='profile'),
       path('update/',views.update,name='update'),


]