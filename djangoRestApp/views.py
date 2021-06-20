from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from djangoRestApp.models import Article
from djangoRestApp.serializers import ArticleSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
#Function Based API Views
# @csrf_exempt
# def article_list(request):
#     if request.method == 'GET':
#         artle = Article.objects.all()
#         serializer = ArticleSerializer(artle, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)      


# @csrf_exempt
# def article_detail(request,pk):
#     try:
#         artcle = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = ArticleSerializer(artcle)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data=JSONParser().parse(request)
#         serializer = ArticleSerializer(artcle, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, starus=404)

#     elif request.method == 'DELETE':
#         artcle.delete()
#         return HttpResponse(status=201)

#Class Based Views
class Articla_list(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'article.html'

    def get(self, request):
        artle = Article.objects.all()
        serializer = ArticleSerializer(artle, many=True)
        return Response({'artle':artle,'serializer':serializer})

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetails(APIView):
    def get_object(self, pk):
        try:
            return get_object_or_404(Article, pk=pk)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        artle = self.get_object(pk)
        serializer = ArticleSerializer(artle)
        return Response(serializer.data)


    def put(self, request, pk):
        artle = self.get_object(pk)
        serializer = ArticleSerializer(artle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        artle = self.get_object(pk)
        artle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""
#api view Decorator
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        artle = Article.objects.all()
        serializer = ArticleSerializer(artle, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
    try:
        artcle = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(artcle)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(artcle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        artcle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""
