"""ams URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from ams import views 
from login import views as loginviews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name = 'home_page'),
    path('contact_us',views.contact_us),
    path('user_list/',views.user_list, name = 'users'),
    path('mark_attendance/',views.mark_attendance, name= 'mark_attendance'),
    path('',views.attendance_app, name  = 'attendance_app'),
    path('register/',loginviews.register, name = 'register'),
    path('login/',loginviews.loginpage, name = 'login'),
    path('attendance_history/',views.attendance_history, name = 'attendance_history'),
    path('logout/',loginviews.logout_user, name = 'logout'),
    path('form/',views.form, name = 'form'),
    path('employees_list/',views.employees_list, name = 'employees_list'),
    path('my_profile/', views.my_profile, name = 'my_profile'),
    ]
