from django.conrib.auth.forms import UserCreationForm
from shortcuts import render

def Signupform(request):
  sForm = UserCreationForm()