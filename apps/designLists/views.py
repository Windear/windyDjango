from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from werkzeug.security import generate_password_hash
from designLists import models
import json


# Create your views here.
#获取全部设计列表
def designLists(request):
    lists = models.Desgin.objects.order_by("-createtime")
    data = serializers.serialize("json", lists)
    return HttpResponse(data)


# 设计分类
def get_design_cate(request):
    design_cate = [{"text": u"UI设计", "val": 1}, {"text": u"插画/原画", "val": 2}, {"text": u"平面设计", "val": 3},
                   {"text": u"3D设计", "val": 4}, {"text": u"动效设计", "val": 5}]
    data = json.dumps(design_cate)
    return HttpResponse(data)



# 设计列表
def get_design_list(request):

    catelist = models.Desgin.objects.values_list('cate')
    catelength = set(catelist)
    dslis = []
    i = 0
    for a in catelength:
        i = i + 1
        design_list = models.Desgin.objects.filter(cate=i)
        lis = {}
        dic2 = []
        for item in design_list:
            dic = {'cate': item.cate, 'projectId': item.id, 'listText': item.title,
                   'listImg': str(item.picture),
                   'listDate': item.dgndatetime
                   }
            dic2.append(dic)
            lis.update({'cate': i, 'list': dic2})
        dslis.append(lis)
    data = json.dumps(dslis)
    return HttpResponse(data)


# 项目列表
def post_project_list(request):
    if request.method == "POST":
        project_list = models.Desgin.objects.values("dgndatetime", "id")
        # n是获取传过来的参数的年份，取数字
        n = json.loads(request.body)['year']
        yearsProject = []
        for a in project_list:
            # year 是 获取查询到的所有的年份，去数字
            year = a['dgndatetime'].split("年")[0]
            # 从所有的年份中筛选传过来的年份
            if year == n:
                yearList = models.Desgin.objects.filter(id=a['id'])
                for item in yearList:
                    yearListDic = {
                        "projectImg": str(item.picture),
                        "projectTitle": item.title,
                        "projectText": item.introduction,
                        "projectId": item.id
                    }
                    yearsProject.append(yearListDic)
        data = json.dumps(yearsProject)
        return HttpResponse(data)


# 设计详情
def get_design_detail(request, id):
    design_detal = models.Desgin.objects.get(id=int(id))
    dedata = {"projectPic": str(design_detal.picture), "projectTitle": design_detal.title,
              "projectDate": design_detal.dgndatetime, "projectCopyright": design_detal.copyright,
              "projectSynopsis": design_detal.introduction, "projectDetail": design_detal.content}
    data = json.dumps(dedata)
    return HttpResponse(data)


# 首页项目案例列表
def get_case_list(request):
    case_list = []
    caseId = [1, 2, 3, 6,7,9, 10, 23,17, 28, 20, 14]
    for i in caseId:
        case = models.Desgin.objects.get(id=int(i))
        caseData = {
            "caseId": case.id,
            "caseImg": str(case.picture),
            "caseTitle": case.title,
            "caseDate": case.dgndatetime
        }
        case_list.append(caseData)
    #print(case_list)
    data = json.dumps(case_list)
    return HttpResponse(data)
