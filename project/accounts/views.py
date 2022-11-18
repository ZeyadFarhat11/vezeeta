from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.

def doctor_list(request):
    return render(request, 'user/doctor_list.html',{'doctors':Profile.objects.all()})

def doctor_detail(request,slug):
    return render(request, 'user/doctors_detail.html',{'doctor_detail':Profile.objects.get(slug=slug)})