from django.contrib.auth.models import User
from user_profile.models import Profile
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView, DeleteView, UpdateView, ListView
from user_profile.forms import AuthUserForm

# @login_required
# def profile(request, username):
#     user = get_object_or_404(User, username=username)
#     return render(
#         request, "user/profile.html", {'user': user}
#     )
from home.models import Article


class UserDeleteView(DeleteView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "user/delete_profile.html"
    success_url = "user/successfully_deleted_profile.html"


class UserUpdateView(UpdateView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = "user/edit_profile.html"
    context_object_name = "user"
    fields = ["username", "first_name", "last_name"]
    success_url = "/articles/"


class ProfileUpdateView(UpdateView):
    model = Profile
    slug_field = 'username'
    slug_url_kwarg = 'profile'
    template_name = 'user/edit_profile_details.html'
    context_object_name = 'profile'
    fields = ['country', 'phone']
    success_url = 'articles'


class UserListView(ListView):
    model = User
    template_name = 'user/all_profiles.html'
    ordering = 'username'
    context_object_name = 'user'


class UserDetailView(DetailView):
    model = User
    template_name = "user/profile.html"
    slug_field = "username"
    slug_url_kwarg = 'username'
    context_object_name = "user"

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        from home.models import Article
        context['articles'] = Article.objects.filter(author=context["user"])
        return context


class UserLoginView(LoginView):
    template_name = 'user/login.html'
    form_class = AuthUserForm
    success_url = 'user/profiles.html'

# @login_required
# def edit_profile(request, username):
#     print(request.POST)
#     user = get_object_or_404(User, username=username)
#     if request.method == 'POST':
#         user.username = request.POST.get('username')
#         profile = user.profile
#         profile.phone = request.POST.get('phone')
#         profile.country = request.POST.get('country')
#         user.save()
#         profile.save()
#     return render(
#         request, "user/edit_profile.html", {'user': user}
#     )
#
# @login_required
# def delete_profile(request, username):
#     print(request.POST)
#     """"
#     Функция удаляет пользователя при запросе POST
#     и возвращает кнопку на удаление при GET
#     """
#     user = get_object_or_404(User, username=username)
#     if request.method == 'POST':
#         user.delete()
#         return render(request, 'user/successfully_deleted_profile.html')
#     return render(
#         request, 'user/delete_profile.html', {'user': user}
#     )
