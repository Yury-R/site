from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.generics import ListAPIView


from home.models import Article
from django.views.generic import ListView, DetailView, UpdateView


def home(request):
    return render(request, 'home.html')



# def debug(request):
#     page = request.GET.get('page')
#     return HttpResponse(f"This is debug URL. Page number {page}")


# @login_required
# def all_articles(request):
#     print(request.user)
#     if request.user.is_authenticated:
#         articles = Article.objects.all()
#         return render(
#             request, "articles.html", {"articles": articles},
#         )
#     else:
#         return HttpResponse("You are not logged in.")


# @login_required
# def get_article(request, pk: int):
#     article = get_object_or_404(Article, pk=pk)
#     return render(
#         request, "article.html", {"obj": article}
#                   )


class ArticleDetailView(DetailView):
    model = Article
    template_name = "article.html"
    pk_url_kwarg = 'pk'
    context_object_name = 'obj'

class ArticleListView(ListView):
    model = Article
    template_name = 'articles.html'
    ordering = 'title'
    context_object_name = 'articles'

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = "edit_article.html"
    slug_field = 'title'
    slug_url_kwarg = 'title'
    success_url = "/articles/"
    context_object_name = 'article'
    fields = ['title', 'content', 'author']


#
# @login_required
# def edit_article(request, ):
#     article = get_object_or_404(Article, pk=int)
#     if request.method == 'POST':
#         article.id = request.POST.get('id')
#         article.title = request.POST.get('title')
#         article.content = request.POST.get('content')
#         article.save()
#     return render(
#         request, "edit_article.html", {"obj": article}
#     )

