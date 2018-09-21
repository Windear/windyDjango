from django.shortcuts import render, HttpResponse
from resources import models
from django.core import serializers
from django.db.models import Count
import json


# Create your views here.
# 设计分类
def get_resources_cate(request):
    resources_cate = models.Resources.CATEGORY_TYPE
    dic_data = []
    for cate in resources_cate:
        dic_data.append({'num': cate[0], 'val': cate[-1]})
    # print(dicData)
    data = json.dumps(dic_data)
    return HttpResponse(data)


# 获取素材列表
def get_resources_list(request, cate):
    if cate == 0 or cate == False:
        cate_list = models.Resources.objects.order_by("-createtime")
    else:
        cate_list = models.Resources.objects.filter(cate=int(cate)).order_by("-createtime")

    resources_data = []
    for list in cate_list:
        data = {
            "resourcesImg": str(list.picture),
            "resourcesTitle": list.title,
            "resourcesType": list.file_type,
            "resourcesId": list.id
        }
        resources_data.append(data)
    if resources_data:
        return HttpResponse(json.dumps(resources_data))
    else:
        err = {
            "msg": "没有数据",
            "state": "err"
        }
        return HttpResponse(json.dumps(err))


# 获取素材详情
def get_resources_details(request, id):
    resources_details = models.Resources.objects.filter(id=int(id))

    """
    返回 title、copyright、picture、content、tag、download_address、
    """
    details = []
    for item in resources_details:
        data = {"resourcesPic": str(item.picture), "resourcesTitle": item.title,
                "resourcesCopyright": item.copyright, "resourcesDetail": item.content,
                "resourcesTag": item.tag,
                "resourcesDownload": str(item.download_address)}
        details.append(data)
        # print(details)
    if details:
        return HttpResponse(json.dumps(details[0]))
    else:
        err = {
            "msg": "没有数据",
            "state": "err"
        }
        return HttpResponse(json.dumps(err))


# 获取素材网盘链接
def get_resources_cloud(request, id):
    resources_cloud = models.CloudDrive.objects.filter(resources_id=int(id))
    cloud = []
    for item in resources_cloud:
        data = {
            "drive_type": item.drive_type,
            "drive_url": item.drive_url,
            "drive_pw": item.drive_pw
        }
        cloud.append(data)
    if cloud:
        return HttpResponse(json.dumps(cloud))
    else:
        err = {
            "msg": "没有数据",
            "state": "err"
        }
        return HttpResponse(json.dumps(err))


# 获取分类
def get_resources_format(request):
    # format_list = models.Resources.objects.values_list('file_type', flat=True).annotate(Count('file_type'))
    format_list = models.Resources.objects.values_list('file_type', flat=True).annotate(Count('file_type'))
    data = list(format_list)
    format_newlist = []
    for items in data:
        items = items.split(',')
        for item in items:
            if item not in format_newlist:
                format_newlist.append(item)
    # format_newlist = data
    # data = list(format_list)
    #print(format_newlist)
    return HttpResponse(json.dumps(format_newlist))


# 获取所传的分类素材列表
def get_resources_format_list(request):
    if request.method == "POST":
        type = json.loads(request.body)['type']
        cate = json.loads(request.body)['cate']
        if cate == 0 or cate == False:
            format_list = models.Resources.objects.filter(file_type__icontains=type).order_by("-createtime")
        else:
            format_list = models.Resources.objects.filter(file_type__icontains=type, cate=int(cate)).order_by(
                "-createtime")

        resources_data = []
        for list in format_list:
            data = {
                "resourcesImg": str(list.picture),
                "resourcesTitle": list.title,
                "resourcesType": list.file_type,
                "resourcesId": list.id
            }
            resources_data.append(data)
        if resources_data:
            print(resources_data)
            return HttpResponse(json.dumps(resources_data))
        else:
            err = {
                "msg": "没有数据",
                "state": "err"
            }
            return HttpResponse(json.dumps(err))


# 素材点击量
def get_resources_looks(request, id):
    resources = models.Resources.objects.get(id=int(id))
    resources.looked_num = resources.looked_num + 1
    models.Resources.objects.filter(id=int(id)).update(looked_num=resources.looked_num)
    # print(resources.looked_num)
    data = {
        "looked_num": resources.looked_num,
        "state": "ok"
    }
    return HttpResponse(json.dumps(data))


# 素材下载量
def get_resources_downloads(request, id):
    resources = models.Resources.objects.get(id=int(id))
    resources.download_num = resources.download_num + 1
    models.Resources.objects.filter(id=int(id)).update(download_num=resources.download_num)
    # print(resources.looked_num)
    data = {
        "download_num": resources.download_num,
        "state": "ok"
    }
    return HttpResponse(json.dumps(data))


#最新素材8条
def get_new_resources(request):
    cate_list = models.Resources.objects.order_by("-createtime")[:8]
    resources_data = []
    for list in cate_list:
        data = {
            "resourcesImg": str(list.picture),
            "resourcesTitle": list.title,
            "resourcesType": list.file_type,
            "resourcesId": list.id
        }
        resources_data.append(data)
    if resources_data:
        return HttpResponse(json.dumps(resources_data))
    else:
        err = {
            "msg": "没有数据",
            "state": "err"
        }
        return HttpResponse(json.dumps(err))
