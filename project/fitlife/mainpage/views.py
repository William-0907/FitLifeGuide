from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'mainpage/home.html')

def test(request):
    return render(request, 'mainpage/test.html')



