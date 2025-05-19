from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm

from django.shortcuts import render, redirect
from .models import EmailOTP
from .utils import generate_otp, send_otp_email
from django.contrib.auth.models import User






def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})




# views.py

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            otp_code = generate_otp()
            EmailOTP.objects.create(user=user, code=otp_code)
            send_otp_email(user.email, otp_code)
            request.session['pre_2fa_user_id'] = user.id
            return redirect('verify_otp')
    return render(request, 'users/login.html')

def verify_otp_view(request):
    user_id = request.session.get('pre_2fa_user_id')
    if not user_id:
        return redirect('login')

    if request.method == 'POST':
        input_code = request.POST['otp']
        otp_entry = EmailOTP.objects.filter(user_id=user_id, code=input_code, is_verified=False).first()
        if otp_entry:
            otp_entry.is_verified = True
            otp_entry.save()
            user = User.objects.get(id=user_id)
            login(request, user)
            return redirect('dashboard')  # Or home page
    return render(request, 'verify_otp.html')










def logout_view(request):
    logout(request)
    return redirect('login')

