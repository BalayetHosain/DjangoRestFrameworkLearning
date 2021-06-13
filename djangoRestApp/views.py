from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from djangoRestApp.models import Article
from djangoRestApp.serializers import ArticleSerializer

@csrf_exempt
def article_list(request):
    if request.method == 'GET':
        artle = Article.objects.all()
        serializer = ArticleSerializer(artle, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)      


@csrf_exempt
def article_detail(request,pk):
    try:
        artcle = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ArticleSerializer(artcle)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data=JSONParser().parse(request)
        serializer = ArticleSerializer(artcle, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, starus=404)

    elif request.method == 'DELETE':
        artcle.delete()
        return HttpResponse(status=201)





