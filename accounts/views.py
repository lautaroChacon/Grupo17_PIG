from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        errors = form.errors
        return render(request, 'accounts/signup.html', {'errors': errors})
    else:
        return render(request, 'accounts/signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            errors = "Nombre de usuario o contraseña incorrectos."
            return render(request, 'accounts/login.html', {'errors': errors})
    return render(request, 'accounts/login.html')


def logout_view(request):
    logout(request)
    return redirect('index')