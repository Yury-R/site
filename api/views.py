from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework.pagination import LimitOffsetPagination

from home.models import Article

from api.pagination import CustomPagination

from api.permissions import IsAuthorOrReadOnly, IsUserOrReadOnly

from api.serializers import ArticleSerializer, UserSerializer



class ArticleViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly, )
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = CustomPagination
    filter_backends = (SearchFilter, OrderingFilter, )
    search_fields = ('title', 'content')


class UserViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'
    pagination_class = LimitOffsetPagination
    filter_backends = (SearchFilter, OrderingFilter, )
    search_fields = ('first_name', 'last_name')


# class ArticleListAPIView(ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#
# class ArticleDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#
# class UserListView(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     lookup_field = 'username'
