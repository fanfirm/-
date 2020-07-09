import random
import re
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from .models import top_info


# Create your views here.


def create_user(request):
    for u in range(1, 31):
        user = 'user{}'.format(u)
        score = random.randint(1, 10000000)
        if top_info.objects.filter(user=user):
            continue
        twz = top_info.objects.create(user=user, score=score)
        twz.save()

    items = top_info.objects.all().values()
    dic = dict()
    j = 1
    for i in items:
        dic[j] = i
        j += 1
    return JsonResponse(dic)


def api_one(request, user, new_score):
    if not 1 < int(new_score) < 10000000:
        return HttpResponse('新成绩不合法')
    if not top_info.objects.filter(user=user):
        twz = top_info.objects.create(user=user, score=new_score)
        twz.save()
    items = top_info.objects.filter(user=user)
    items.update(score=new_score)
    query_doc = top_info.objects.all().values()
    dic = dict()
    j = 1
    for query in query_doc:
        dic[j] = query
        j += 1
    return JsonResponse(dic)


def api_two(request, user, rank):
    if not top_info.objects.filter(user=user):
        return HttpResponse('用户不合法')
    pretty = re.match(r'\d+[-]\d+', rank)
    if not pretty:
        return HttpResponse('查询名次段不合法')
    users = top_info.objects.filter(user=user).values()[0]
    rank_num = rank.split('-')
    start = int(rank_num[0])
    end = int(rank_num[1])
    query = top_info.objects.order_by('-score')
    items = query[start:end + 1]
    j = 0
    for qu in query:
        j += 1
        if qu.user == user:
            print(j)
            break
    dic = dict()
    for i in items:
        ddic = dict()
        ddic['user'] = 'user{}'.format(start)
        ddic['score'] = i.score
        dic[start] = ddic
        start += 1
    querydict = {}
    querydict['query1'] = dic
    querydict['query2'] = {j: users}
    return JsonResponse(querydict)







