from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import DetailView, DeleteView, UpdateView


# @login_required
# def profile(request, username):
#     user = get_object_or_404(User, username=username)
#     return render(
#         request, "user/profile.html", {'user': user}
#     )

class UserDetailView(DetailView):
    model = User
    template_name = "user/profile.html"
    slug_field = "username"
    slug_url_kwarg = 'username'
    context_object_name = "user"

    # def get_context_data(self, username, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['user'] = get_object_or_404(User, username=username)
    #     return context


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
    fields = ["username"]
    success_url = "/articles/"


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
