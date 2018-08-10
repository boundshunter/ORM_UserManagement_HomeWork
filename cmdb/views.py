from django.shortcuts import render, redirect, HttpResponse
# from django.db import models
from cmdb import models
# Create your views here.


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        user = request.POST.get('username')
        pwd = request.POST.get('pwd')
        obj = models.UserInfo.objects.filter(username=user, password=pwd).first()
        if obj:
            return render(request, 'user_info.html')
        else:
            return redirect('/cmdb/login/')
    else:
        return redirect('/cmdb/login/')


def user_info(request):
    pass


def group_info(request):
    pass


def user_detail(request):
    pass


def orm(request):
    # models.UserInfo.objects.create(username='admin', password='abc', gender=0, age=25, job='IT')
    # models.UserInfo.objects.all().delete()
    return HttpResponse('Data Created Successful.')