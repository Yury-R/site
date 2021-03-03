from django.urls import path

from django.conf import settings
from django.conf.urls import static

from home import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('debug/', views.debug, name='debug'),
    path('articles/', views.ArticleListView.as_view(), name='all-articles'),
    path('articles/<int:pk>', views.ArticleDetailView.as_view(), name='get-articles'),
    path('articles/<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='edit-article')
]
