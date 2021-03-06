from django.shortcuts import render, HttpResponse
from macTools import models
from django.core import serializers
from django.db.models import Count
import json, datetime, hashlib


# Create your views here.
class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        # elif isinstance(obj, date):
        #     return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


# 哈希加密
class Hashmd5():
    def md5(val):
        md5 = hashlib.md5()
        md5.update(val.encode('utf-8'))
        print(val)
        return md5.hexdigest()


# 工具点击量
def get_tools_looks(request, id):
    tools = models.Tools.objects.get(id=int(id))
    tools.looked_num = tools.looked_num + 1
    models.Tools.objects.filter(id=int(id)).update(looked_num=tools.looked_num)
    # print(resources.looked_num)
    data = {
        "looked_num": tools.looked_num,
        "state": "ok"
    }
    return HttpResponse(json.dumps(data))


# 工具下载量
def get_tools_downloads(request, id):
    tools = models.Tools.objects.get(id=int(id))
    tools.download_num = tools.download_num + 1
    models.Tools.objects.filter(id=int(id)).update(download_num=tools.download_num)
    # print(resources.looked_num)
    data = {
        "download_num": tools.download_num,
        "state": "ok"
    }
    return HttpResponse(json.dumps(data))


# 获取所有工具类别
def get_tools_cate(request):
    tools_cate = models.Tools.CATEGORY_TYPE
    dic_data = []
    for cate in tools_cate:
        dic_data.append({'num': cate[0], 'val': cate[-1]})
    # print(dicData)
    data = json.dumps(dic_data)
    return HttpResponse(data)


# 获取全部工具列表***
def get_tools_allList(request, cate):
    if cate == 0 or cate == False:
        tools_list = models.Tools.objects.order_by("-create_time")
    else:
        tools_list = models.Tools.objects.filter(cate=int(cate)).order_by("-create_time")

    tools_data = []
    tools_cate = models.Tools.CATEGORY_TYPE
    for list in tools_list:
        tools_version = models.HistoryVersion.objects.filter(tools_id=list.id)
        tools_sys = []
        for item in tools_version:
            if item.drive_type not in tools_sys:
                tools_sys.append(item.drive_type)
        # print(tools_sys)
        data = {
            "toolsIcon": str(list.icon),
            "toolsTitle": list.title,
            "toolsIntroduction": list.introduction,
            "toolsCate": tools_cate[list.cate - 1],
            "toolsId": list.id,
            "toolsSys": tools_sys
        }
        tools_data.append(data)
    if tools_data:
        return HttpResponse(json.dumps(tools_data))
    else:
        err = {
            "msg": "没有数据",
            "state": "err"
        }
        return HttpResponse(json.dumps(err))


# 获取工具详情
def get_tools_details(request, id):
    tools_details = models.Tools.objects.filter(id=int(id))

    """
    返回 title、icon、cate、tag、introduction、new_version、content、looked_num、download_num、create_time
    """
    details = []
    tools_cate = models.Tools.CATEGORY_TYPE
    for item in tools_details:
        data = {"toolsIcon": str(item.icon), "toolsTitle": item.title,
                "toolsCate": tools_cate[item.cate - 1], "toolsTag": item.tag,
                "toolsIntroduction": item.introduction,
                "toolsNewVersion": item.new_version,
                "toolsContent": item.content, "toolsLookedNum": item.looked_num,
                "toolsDownloadNum": item.download_num,
                "sid":Hashmd5.md5(str(item.id) + '.' + item.title)
                # "toolsDownCreateTime": item.create_time,
                }
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
    pass


# 获取工具下载链接
def get_tools_cloud(request, id):
    tools_cloud = models.HistoryVersion.objects.filter(tools_id=int(id)).order_by("-id")
    """
    version、language、update_time、file_size、
    drive_type、drive_url、drive_pw
    """
    tools_language = models.HistoryVersion.LANGUAGE_TYPE
    languageData = {}
    for one in tools_language:
        languageData.update({one[0]: one[-1]})
    cloud = []
    for item in tools_cloud:
        data = {
            "version": item.version,
            "language": languageData[item.language],
            "update_time": json.dumps(item.update_time, cls=CJsonEncoder).split('\"')[1],
            "file_size": item.file_size,
            "drive_type": item.drive_type,
            "drive_url": item.drive_url,
            "drive_pw": item.drive_pw
        }
        # print(languageData['EN'])
        cloud.append(data)
    if cloud:
        return HttpResponse(json.dumps(cloud))
    else:
        err = {
            "msg": "没有数据",
            "state": "err"
        }
        return HttpResponse(json.dumps(err))


# 获取最近6条工具信息
def get_new_tools(request):
    tools_list = models.Tools.objects.order_by("-create_time")[:6]
    tools_data = []
    tools_cate = models.Tools.CATEGORY_TYPE
    for list in tools_list:
        tools_version = models.HistoryVersion.objects.filter(tools_id=list.id)
        tools_sys = []
        for item in tools_version:
            if item.drive_type not in tools_sys:
                tools_sys.append(item.drive_type)
        # print(tools_sys)
        data = {
            "toolsIcon": str(list.icon),
            "toolsTitle": list.title,
            "toolsIntroduction": list.introduction,
            "toolsCate": tools_cate[list.cate - 1],
            "toolsId": list.id,
            "toolsSys": tools_sys
        }
        tools_data.append(data)
    if tools_data:
        return HttpResponse(json.dumps(tools_data))
    else:
        err = {
            "msg": "没有数据",
            "state": "err"
        }
        return HttpResponse(json.dumps(err))
