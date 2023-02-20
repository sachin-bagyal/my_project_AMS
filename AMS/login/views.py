from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout

# Create your views here.



def register(request):
    my_form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,username + ' has been created successfully')
            return redirect('login')
    data = {
        'myform':my_form
    }
    return render(request,'register.html',data)

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password = password) 
        if user is not None:
            login(request,user)
            request.session['login_msg'] = 'hello user'
            return redirect('home_page')
        else :
            messages.info(request,username +' invalid username or password')
            return redirect('login')
        
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')


