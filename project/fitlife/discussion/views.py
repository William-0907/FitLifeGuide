from django.shortcuts import render

# Create your views here.

def discussion(request):
    return render(request, 'discussion/discussions.html')