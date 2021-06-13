
from django.urls import path
from djangoRestApp.views import article_list, article_detail

urlpatterns = [
    path('articleListAPI/', article_list, name='articleListAPI'),
    path('article_detailAPI/<int:pk>/', article_detail, name='article_detailAPI'),
]
