from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import login as slogin, authenticate, logout as slogout


# Create your views here.
def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        message = "please check forms！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                slogin(request, user)
                print("OK................")
                return redirect('/index')
            else:
                message = "loging error"
                return render(request, 'login.html', locals())
        return render(request, 'login.html', locals())
    else:
        login_form = LoginForm()
        return render(request, 'login.html', locals())


def logout(request):
    slogout(request)
    return redirect('login/')
