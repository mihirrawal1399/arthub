from django.shortcuts import render
from django.contrib import auth
# Create your views here.


def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')
