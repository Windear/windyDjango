from django.shortcuts import render, HttpResponse
from blog import models
from django.core import serializers
from django.db.models import Count
import json, datetime


# Create your views here.
class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        # elif isinstance(obj, date):
        #     return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


# 文章点击量
def get_blog_looks(request, id):
    tools = models.BlogArticle.objects.get(id=int(id))
    tools.looked_num = tools.looked_num + 1
    models.BlogArticle.objects.filter(id=int(id)).update(looked_num=tools.looked_num)
    # print(resources.looked_num)
    data = {
        "looked_num": tools.looked_num,
        "state": "ok"
    }
    return HttpResponse(json.dumps(data))


# 文章类型获取
def get_blog_cate(request):
    tools_cate = models.BlogArticle.CATEGORY_TYPE
    dic_data = []
    for cate in tools_cate:
        dic_data.append({'num': cate[0], 'val': cate[-1]})
    # print(dicData)
    data = json.dumps(dic_data)
    return HttpResponse(data)


# 文章列表获取
def get_blog_allList(request, cate):
    if cate == 0 or cate == False:
        tools_list = models.BlogArticle.objects.order_by("-create_time")
    else:
        tools_list = models.BlogArticle.objects.filter(cate=int(cate)).order_by("-create_time")

    article_data = []
    article_cate = models.BlogArticle.CATEGORY_TYPE
    article_original = models.BlogArticle.IS_ORIGINAL
    for list in tools_list:
        data = {
            "articlePicture": str(list.picture),
            "articleTitle": list.title,
            "articleIntroduction": list.introduction,
            "articleTag": list.tag,
            "articleCate": article_cate[list.cate - 1],
            "articleAuthor": list.author,
            "articleOriginal": article_original[list.is_original - 1],
            "articleLookedNum": list.looked_num,
            "articleId": list.id,
            "createTime": json.dumps(list.create_time, cls=CJsonEncoder).split('\"')[1].split(' ')[0],
        }
        article_data.append(data)
    if article_data:
        return HttpResponse(json.dumps(article_data))
    else:
        err = {
            "msg": "没有数据",
            "state": "err"
        }
        return HttpResponse(json.dumps(err))


# 获取文章详情
def get_blog_details(request, id):
    blog_details = models.BlogArticle.objects.filter(id=int(id))

    """
    返回 title、icon、cate、tag、introduction、new_version、content、looked_num、download_num、create_time
    """
    details = []
    article_cate = models.BlogArticle.CATEGORY_TYPE
    article_original = models.BlogArticle.IS_ORIGINAL
    for list in blog_details:
        data = {"articlePicture": str(list.picture),
                "articleTitle": list.title,
                "articleIntroduction": list.introduction,
                "articleTag": list.tag,
                "articleCate": article_cate[list.cate - 1],
                "articleAuthor": list.author,
                "articleOriginal": article_original[list.is_original - 1],
                "articleLookedNum": list.looked_num,
                "articleContent": list.content,
                "articleId": list.id,
                "createTime": json.dumps(list.create_time, cls=CJsonEncoder).split('\"')[1].split(' ')[0],
                }
        # print(json.dumps(list.create_time, cls=CJsonEncoder).split('\"')[1].split('')[0])
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


# 获取最近三条文章
def get_new_blog(request):
    tools_list = models.BlogArticle.objects.order_by("-create_time")[:5]
    article_data = []
    article_cate = models.BlogArticle.CATEGORY_TYPE
    article_original = models.BlogArticle.IS_ORIGINAL
    for list in tools_list:
        data = {
            "articlePicture": str(list.picture),
            "articleTitle": list.title,
            "articleIntroduction": list.introduction,
            "articleTag": list.tag,
            "articleCate": article_cate[list.cate - 1],
            "articleAuthor": list.author,
            "articleOriginal": article_original[list.is_original - 1],
            "articleLookedNum": list.looked_num,
            "articleId": list.id,
            "createTime": json.dumps(list.create_time, cls=CJsonEncoder).split('\"')[1].split(' ')[0],
        }
        article_data.append(data)
    if article_data:
        return HttpResponse(json.dumps(article_data))
    else:
        err = {
            "msg": "没有数据",
            "state": "err"
        }
        return HttpResponse(json.dumps(err))
