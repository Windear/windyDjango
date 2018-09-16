from django.shortcuts import render, HttpResponse
from macTools import models
from django.core import serializers
from django.db.models import Count
import json

# Create your views here.
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
    models.tools.objects.filter(id=int(id)).update(download_num=tools.download_num)
    # print(resources.looked_num)
    data = {
        "download_num": tools.download_num,
        "state": "ok"
    }
    return HttpResponse(json.dumps(data))