from django.shortcuts import render, redirect, HttpResponse
# from django.db import models
from cmdb import models
# Create your views here.


def business(request):
    v1 = models.Business.objects.all()

    # v QuerySet
    # 列表里面都是对象
    # [obj1(id,caption,code),obj2(..), ..]
    # return HttpResponse('abc')

    v2 = models.Business.objects.all().values('id', 'caption')
    # select id,caption from cmdb_business
    # v1 QuerySet,列表里面元素为字典
    # [{'id':1,'caption':'运维部'},{},{}]

    v3 = models.Business.objects.all().values_list('id', 'caption')
    # v3 Queryset
    # [(1,运维部)，(2,开发部), ..]
    return render(request, 'business.html', {'v1': v1, 'v2': v2, 'v3': v3})


def host(request):
    v1 = models.Host.objects.all()
    return render(request, 'host.html', {'v1': v1})