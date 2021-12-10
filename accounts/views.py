from django.shortcuts import render,redirect
from django .contrib.auth.forms import UserCreationForm
from .forms import NewAuthenticationForm
from django.contrib.auth import login,logout
from . import forms

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        newuserForm = forms.NewUserCreationForm(request.POST)
        if newuserForm.is_valid():
            user = newuserForm.save()
            login(request,user)
            return redirect('pins:list')
    else:
        newuserForm = forms.NewUserCreationForm()
    return render(request,'accounts/signup.html',{'newuserForm':newuserForm})

def login_view(request):
    if request.method == 'POST':
        authenticationForm = NewAuthenticationForm(data=request.POST)
        if authenticationForm.is_valid():
            user = authenticationForm.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('pins:list')
    else:
        authenticationForm = NewAuthenticationForm()
    return render(request,'accounts/login.html',{'authenticationForm':authenticationForm})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('accounts:login')