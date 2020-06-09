from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.views.generic import ListView
from django.views.generic.edit import FormView


from apps.articles.models import Article
from apps.articles.forms import ArticleForm


def main_page(request):
    return render(request, 'pages/main_page.html')


def articles_json(request):
    articles = Article.objects.all().values()
    list_of_articles = [article for article in articles]
    return JsonResponse(list_of_articles, safe=False)


class ArticleListView(ListView):
    model = Article
    template_name = 'articles.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SearchResultsView(View):
    def get(self, request, **kwargs):

        search_q = request.GET.get('search', '')

        if search_q:
            articles = Article.objects.filter(title__icontains=search_q)
        else:
            articles = Article.objects.all()

        context_data = {
            'articles': articles,
        }
        return render(request, 'pages/search.html', context=context_data)


class ArticleFormView(FormView):
    template_name = 'form_article.html'
    form_class = ArticleForm
    success_url = '/articles/search/'

