from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from next_app.forms import Admin_User_Form,Common_User_Form,Admin_User_AddForm,Common_User_AddForm,AndroidAppForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from next_app.models import Admin_User,Common_User,AndroidApp
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request,'gradesApp/index.html')


@login_required
def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    return render(request,'gradesApp/register.html')

def registeradmin(request):
    registered=False
    if request.method=='POST':
        var_adminForm=Admin_User_Form(request.POST)
        var_adminAddForm=Admin_User_AddForm(request.POST)
        if var_adminForm.is_valid()and var_adminAddForm.is_valid():
            adminprimary=var_adminForm.save()
            adminprimary.set_password(adminprimary.password)
            adminprimary.save()
            adminAdd=var_adminAddForm.save(commit=False)
            adminAdd.admin_user=adminprimary
            adminAdd.save()
            registered=True
    else:
        var_adminForm=Admin_User_Form()
        var_adminAddForm=Admin_User_AddForm()
    data={
        'var_adminForm':var_adminForm,
        'var_adminAddForm':var_adminAddForm,
        'registered':registered
        }
    return render(request,'gradesApp/registeradmin.html',data)


def registeruser(request):
    registered=False
    if request.method=='POST':
        var_userForm=Common_User_Form(request.POST)
        var_userAddForm=Common_User_AddForm(request.POST)
        if var_userForm.is_valid()and var_userAddForm.is_valid():
            userprimary=var_userForm.save()
            userprimary.set_password(userprimary.password)
            userprimary.save()
            userAdd=var_userAddForm.save(commit=False)
            userAdd.common_user=userprimary
            userAdd.save()
            registered=True
    else:
        var_userForm=Common_User_Form()
        var_userAddForm=Common_User_AddForm()
    data={
        'var_userForm':var_userForm,
        'var_userAddForm':var_userAddForm,
        'registered':registered}
    return render(request,'gradesApp/registeruser.html',data)
    
def userLogin(request):
    invalidlogin=False
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active')
        else:
            invalidlogin=True
            return redirect('/gradesApp/login/')
    else:
        return render(request,'gradesApp/login.html',{'invalidlogin':invalidlogin})


# from django.shortcuts import render, redirect
# from .models import Admin_User, Common_User
# from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    print("request",request.user)
    try:
        current=Admin_User.objects.get(admin_user=request.user)
        print("current",current)
        is_admin_user = True
    except Admin_User.DoesNotExist:
        current=Common_User.objects.get(common_user=request.user)
        print("current",current)
        is_admin_user = False

    if is_admin_user:
        return redirect('/adminDash/')
    else:
        return redirect('/userDash/')
    return render(request,'gradesApp/dashboard.html')




from django.shortcuts import render, redirect
from .models import Admin_User, Common_User
from django.contrib.auth.decorators import login_required





def adminDash(request):
    return render(request,'gradesApp/adminDash.html')

def userDash(request):
    return render(request,'gradesApp/userDash.html')

def add_android_app(request):
    if request.method == 'POST':
        print("f1")

        # form = AndroidAppForm(request.POST)
        form = AndroidAppForm(request.POST, request.FILES)
        print("f12")
        if form.is_valid():
            print("f3")
            form.save()
            return redirect('app_list')
    else:
        print("f")
        form = AndroidAppForm()
    return render(request, 'gradesApp/add_android_app.html', {'form': form})

from django.contrib.auth.decorators import login_required

# @login_required
def app_list(request):
    apps = AndroidApp.objects.all()
    return render(request, 'gradesApp/app_list.html', {'apps': apps})

def app_list1(request):
    apps = AndroidApp.objects.all()
    return render(request, 'gradesApp/app_list1.html', {'apps': apps})

from django.shortcuts import render, get_object_or_404
def app_detail(request, app_id):
    app = get_object_or_404(AndroidApp, id=app_id)
    return render(request, 'gradesApp/app_detail.html', {'app': app})



# views.py

# from django.shortcuts import render, redirect
from .forms import TaskScreenshotForm

def add_task_screenshot(request):
    if request.method == 'POST':
        form = TaskScreenshotForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user  # Assign the current user to the 'user' field
            form.save()
            return redirect('app_list')  # Replace 'app_list' with the URL name of your app list page
    else:
        form = TaskScreenshotForm()
    return render(request, 'gradesApp/add_task.html', {'form': form})  # Replace 'your_template.html' with your desired template name


def app_list1(request):
    apps = AndroidApp.objects.all()
    return render(request, 'gradesApp/app_list1.html', {'apps': apps})