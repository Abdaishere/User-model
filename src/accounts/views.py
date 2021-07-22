from django.contrib import messages
from django.shortcuts import render,redirect
from .forms import  changeAccount, createAccount
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

def home(request):
    return render(request, "home.html")

def registerUser(request):
    form = createAccount()
    if request.method == 'POST':
        form = createAccount(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            passs = form.cleaned_data.get('password1')
            user = authenticate(request,username=user, password=passs)
            print("user created with username : " + user.get_username())
            login(request, user)
            return redirect('/')
    context = {'form' :form}
    return render(request, "customer_register.html", context)


def registerAdmin(request):
    form = createAccount()
    if request.method == 'POST':
        form = createAccount(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            passs = form.cleaned_data.get('password1')
            user = authenticate(request,username=user, password=passs)
            print("user created with username : " + user.get_username())
            login(request, user)
            return redirect('/')

    context = {'form' :form}
    return render(request, "admin_register.html", context)


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passs = request.POST.get('password')
        user = authenticate(request,username=username, password=passs)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'username or password is incorrect')
    context = {}
    return render(request, 'login.html', context)

def updateProfile(request):
    if request.method == 'POST':
        form = changeAccount(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors)
    elif request.method == "GET":
        form = changeAccount(instance=request.user)
        return render(request, 'Profile.html', {'form': form})

def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password_change.html', {
        'form': form
    })

def logoutUser(request):
    logout(request)
    return redirect('/login')

# def logout(request):
#     if request.session.get('email', None):
#         del request.session['email']
#         del request.session['type']
#         return render(request,"home.html",{})
#     else:
#         return render(request,"login.html",{})