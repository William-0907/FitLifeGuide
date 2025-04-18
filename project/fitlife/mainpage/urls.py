from .views import home,test,discussions
from django.urls import path

urlpatterns = [
    path('', home, name='home',),
    path('test/', test,name='test',),
    path('community/discussions', discussions,name='discussions',),
]