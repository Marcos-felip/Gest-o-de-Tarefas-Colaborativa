from django.urls import path
from myapp.views import login

urlpatterns = [
    path('', login, name='login'),
    ]