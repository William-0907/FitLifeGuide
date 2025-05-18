from .views import home,test
from django.urls import path

urlpatterns = [
    path('home/', home, name='home',),
    path('test/', test,name='test',),
]