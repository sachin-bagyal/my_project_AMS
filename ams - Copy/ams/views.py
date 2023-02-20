from django.db import connection
from datetime import datetime
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth.decorators import login_required 
from django.shortcuts import render
from employees.models import attendance 
from employees.models import employees as emp_model
from django.contrib import messages 
from django.shortcuts import redirect
import random

@login_required(login_url='login')
def home(request):
    data = {'title':'Home page'}
    return render(request,'home.html',data)

def contact_us(request):
    return HttpResponseRedirect('/users/')

def user_list(request):
    return render(request,'user_list.html')

def get_user_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@login_required(login_url='login') 
def mark_attendance(request): 
    current_user_ip = get_user_ip(request) 
    current_user = request.user 
    today = datetime.now() 
    current_date_time = today.strftime('%Y-%m-%d %H:%M:%S') 
    current_date_time2 = today.strftime('%d-%m-%Y %H:%M:%S') 
    current_year = today.strftime('%Y') 
    current_month = today.strftime('%m') 
    current_date = today.strftime('%d') 
    is_timed_out = 'no' 
    is_time_in = 'no' 
    attendance_id = 0 
    visit_counter = request.session.get('visit_counter',0)
    request.session['visit_counter'] = visit_counter + 1
    Todays_attendance = None 
    try: 
        Todays_attendance = attendance.objects.filter(user_id = request.user.id,time_in__year = current_year,time_in__month=current_month,time_in__day = current_date).order_by('-time_in').all()
    except attendance.DoesNotExist:
        Todays_attendance = None
    if Todays_attendance.exists():
        is_time_in = 'yes'
        for item in Todays_attendance:
            is_timed_out = item.is_timed_out
            attendance_id = item.id
    else :
        is_time_in = 'no'
        is_timed_out = 'no'
        attendance_id = 0
    data = {'username': current_user.username, 'date_time' : current_date_time, 'is_time_in' : is_time_in , 'Todays_attendance':Todays_attendance,'is_timed_out':is_timed_out,'attendance_id':attendance_id,'user_ip_address':current_user_ip}
    if request.method=='POST':
        username = request.POST.get('uname')
        date_time = request.POST.get('date_time')
        user_action = request.POST.get('user_action')
        if user_action == 'Time_in':
            #save_data = attendance(user_id= random.randint(1,15),employee_id = random.randint(1,15),time_in = current_date_time,time_out = current_date_time)
            save_data = attendance(user_id= request.user.id,employee_id = random.randint(1,15),time_in = current_date_time,time_out = current_date_time)
            save_data.save()
            return redirect('mark_attendance')
        else :
            id = request.POST.get('Attendance_id')
            user_attendance = attendance.objects.get(id=id)
            user_attendance.is_timed_out = 'yes'
            user_attendance.save()
            return redirect('mark_attendance')
            #save_data = attendance(user_id= random.randint(1,10),employee_id = random.randint(1,15),time_in = current_date_time,time_out = current_date_time)
            #save_data.save()  
        messages.success(request,'Users attendance marked successfully')
    return render(request,'mark_attendance.html', data)

def attendance_history(request):
    attendance_data = attendance.objects.all()
    print(attendance_data.query)
    data = { 'attendance_data':attendance_data }
    return render(request,'attendance_history.html',data)

def attendance_app(request):
    return render(attendance_app)

def logout(request):
    auth.logout(request)
    return render('home.html')    

def form(request):
    return render(request,'form.html')

def employees_list(request):
    if request.user.is_staff :
        employees_data = emp_model.objects.all()
        print(employees_data.query)
        data = { 'employees_data': employees_data }
        return render(request,'employees.html',data)
    else :
        return redirect('home_page')    

def my_profile(request):
    return render(request,'my_profile.html')

