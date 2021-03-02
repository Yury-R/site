from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from home.models import Article
from django.views.generic import TemplateView, ListView, DetailView


# Create your views here.


def home(request):
    return render(request, 'home.html')


def debug(request):
    page = request.GET.get('page')
    return HttpResponse(f"This is debug URL. Page number {page}")


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
    slug_field = "pk"
    slug_url_kwarg = 'pk'
    context_object_name = 'obj'

class ArticleListView(ListView):
    model = Article
    template_name = 'articles.html'
    ordering = 'title'
    context_object_name = 'articles'

@login_required
def edit_article(request, ):
    article = get_object_or_404(Article, pk=int)
    if request.method == 'POST':
        article.id = request.POST.get('id')
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
    return render(
        request, "edit_article.html", {"obj": article}
    )

