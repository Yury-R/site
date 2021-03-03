from django.urls import path

from api import views

urlpatterns = [
    path('test/', views.test),
    path('api/articles/', views.ArticleListAPIView.as_view()),
    # path('', views.home, name='home'),
    # # path('debug/', views.debug, name='debug'),
    # path('articles/', views.ArticleListView.as_view(), name='all-articles'),
    # path('articles/<int:pk>', views.ArticleDetailView.as_view(), name='get-articles'),
    # path('articles/<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='edit-article'),
    # path('<str:username>/', views.UserDetailView.as_view(), name='user-profile'),
    # path('<str:username>/edit/', views.UserUpdateView.as_view(), name='edit-profile'),
    # path('<str:username>/delete/', views.UserDeleteView.as_view(), name='delete-profile'),
]