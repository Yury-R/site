from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register('articles', views.ArticleViewSet, basename='articles')
router.register('users', views.UserViewSet, basename='users')

"""
/articles/  GET / LIST
/articles/  POST / CREATE
/articles/<int:pk>/ GET / Read
/articles/<int:pk>/ DELETE/ Delete
/articles/<int:pk>/ PUT/ Update
"""


urlpatterns = [
    path('', include(router.urls)),
    # path('api/articles/', views.ArticleListAPIView.as_view(), name='api-all-articles'),
    # path('api/articles/<int:pk>', views.ArticleDetailAPIView.as_view(), name='api-one-article'),
    # path('api/users/', views.UserListView.as_view(), name='api-users'),
    # path('api/users/<str:username>', views.UserViewSet.as_view(), name='api-one-user')
]
