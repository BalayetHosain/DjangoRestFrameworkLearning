from django.db.models import fields
from djangoRestApp.models import *
from rest_framework import serializers

#Normal serializers
# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     authorname = serializers.CharField(max_length=255)
#     email = serializers.EmailField(max_length=30)
#     date = serializers.DateTimeField()

#     def create(self, validated_data):
#         return Article.objects.create(validated_data)

#     def update(self, instance,validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.authorname = validated_data.get('authorname', instance.authorname)
#         instance.email = validated_data.get('email', instance.email)
#         instance.date = validated_data.get('date', instance.date)
#         instance.save()
#         return instance

class ArticleSerializer(serializers.Serializer):
    class Meta:
        model = Article
        # fields = '__all__'
        fields = ['title','authorname','email','date']


