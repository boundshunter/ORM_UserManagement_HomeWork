from django.shortcuts import render, redirect, HttpResponse
import json
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
    if request.method == "GET":
        v1 = models.Host.objects.all()
        v2 = models.Host.objects.filter(nid__gt=0).values('nid', 'hostname', 'b_id', 'b__caption')
        # for row in v2:
        #     print(row['nid'], row['hostname'], row['b_id'], row['b__caption'])
        v3 = models.Host.objects.filter(nid__gt=0).values_list('nid', 'hostname', 'b_id', 'b__caption')
        b_list = models.Business.objects.all()
        return render(request, 'host.html', {'v1': v1, 'v2': v2, 'v3': v3, 'b_list': b_list})
    elif request.method == 'POST':
        h = request.POST.get('hostname')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('b_id')
        print(h, i, p, b)
        models.Host.objects.create(hostname=h, ip=i, port=p, b_id=b)
        return redirect('/cmdb/host')


# def commit_ajax(request):
#     h = request.POST.get('hostname')
#     i = request.POST.get('ip')
#     p = request.POST.get('port')
#     b = request.POST.get('b_id')
#     return HttpResponse("ok")


# def test_ajax(request):
#     h = request.POST.get('hostname')
#     i = request.POST.get('ip')
#     p = request.POST.get('port')
#     b = request.POST.get('bid')
#     print(h, i, p, b)
#
#     if h and len(h)>5:
#         models.Host.objects.create(hostname=h, ip=i, port=p, b_id=b)
#         return HttpResponse("ok")
#     else:
#         return HttpResponse(h+" is to short")

def test_ajax(request):
    ret = {'status': None, 'error':None, 'data':None}
    try:
        h = request.POST.get('hostname')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('bid')
        print(h, i, p, b)

        if h and len(h)>5:
            models.Host.objects.create(hostname=h, ip=i, port=p, b_id=b)
            # return HttpResponse("ok")
            ret['status'] = True
            ret['data'] = "OK"
        else:
            # return HttpResponse(h+" is to short")
            ret['staus'] = False
            ret['error'] = "hostname is too short"
    except Exception as e:
        ret['status'] = False
        ret['error'] = "请求错误"

    return HttpResponse(json.dumps(ret))


def app(request):
    if request.method == 'GET':
        app_list = models.Application.objects.all()
        host_list = models.Host.objects.all()
        return render(request, 'app.html', {'app_list': app_list, 'host_list': host_list})
    elif request.method == 'POST':
        app_name = request.POST.get('app_name')
        host_list = request.POST.getlist('host_list')
        # print(app_name)
        # print(host_list)
        obj = models.Application.objects.create(name=app_name)
        obj.r.add(*host_list)
        return redirect("/cmdb/app/")


def ajax_app(request):
    ret = {'status': True, 'error': None, 'data': None}
    app_name = request.POST.get('app_name')
    # ******* 传入列表，使用getlist *******
    host_list = request.POST.getlist('host_list')
    print(app_name, host_list)
    obj = models.Application.objects.create(name=app_name)
    obj.r.add(*host_list)
    return HttpResponse(json.dumps(ret))
