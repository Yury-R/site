from django.urls import path

from user_profile import views


urlpatterns = [
      path('profiles/', views.UserListView.as_view(), name='profiles'),
      path('login/', views.UserLoginView.as_view(), name='login_page'),
      path('<str:username>/', views.UserDetailView.as_view(), name='user-profile'),
      path('<str:username>/edit/', views.UserUpdateView.as_view(), name='edit-profile'),
      path('<str:username>/edit2/', views.ProfileUpdateView.as_view(), name='edit-profile-details'),
      path('<str:username>/delete/', views.UserDeleteView.as_view(), name='delete-profile'),
]
