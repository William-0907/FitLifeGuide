from .views import discussion
from django.urls import path

urlpatterns = [
    path('community/discussion', discussion,name='discussion',),
]