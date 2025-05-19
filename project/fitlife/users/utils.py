# utils.py
from django.core.mail import send_mail
import random

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_email(user_email, otp_code):
    send_mail(
        subject="Your 2FA Code",
        message=f"Your 2FA verification code is: {otp_code}",
        from_email="no-reply@yourdomain.com",
        recipient_list=[user_email],
        fail_silently=False,
    )
