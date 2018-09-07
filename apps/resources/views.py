from django.shortcuts import render, HttpResponse
from resources import models
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
            # "resourcesText": list.introduction,
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
