from django.urls import path

from api import views


urlpatterns = [
    path('api/articles/', views.ArticleListAPIView.as_view(), name='api-all-articles'),
    path('api/articles/<int:pk>', views.ArticleDetailAPIView.as_view(), name='api-one-article'),
    path('api/users/', views.UserListView.as_view(), name='api-users'),
    path('api/users/<str:username>', views.UserDetailAPIView.as_view(), name='api-one-user')
]
