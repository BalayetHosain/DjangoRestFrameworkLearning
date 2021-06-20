
from django.urls import path
# from djangoRestApp.views import article_list, article_detail
from djangoRestApp.views import Articla_list, ArticleDetails

urlpatterns = [
    # path('articleListAPI/', article_list, name='articleListAPI'),
    # path('article_detailAPI/<int:pk>/', article_detail, name='article_detailAPI'),
    path('Articla_listAPI/', Articla_list.as_view(), name='Articla_listAPI'),
    path('ArticleDetailsAPI/<int:pk>/', ArticleDetails.as_view(), name='ArticleDetailsAPI'),
]
