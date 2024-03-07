from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from .forms import RegistrationForm, LoginForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                if user.role == 'student':
                    return redirect('student_dashboard')
                elif user.role == 'staff':
                    return redirect('staff_dashboard')
                elif user.role == 'admin':
                    return redirect('admin_dashboard')
                elif user.role == 'editor':
                    return redirect('editor_dashboard')
            else:
                messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Form is invalid.")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})




@login_required
def student_dashboard(request):
    return render(request, 'student.html')

@login_required
def staff_dashboard(request):
    return render(request, 'staff.html')

@login_required
def admin_dashboard(request):
    return render(request, 'admin.html')

@login_required
def editor_dashboard(request):
    return render(request, 'editor.html')
