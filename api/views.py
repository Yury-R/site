from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.generics import ListAPIView, ListCreateAPIView

from api.serializers import ArticleSerializer
from home.models import Article


def test(request):
    return JsonResponse(
        {
            "date": "2020-03-03",
            "status": "alone"
        }
    )


class ArticleListAPIView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
