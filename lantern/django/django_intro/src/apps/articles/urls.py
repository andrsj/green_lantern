from django.urls import path

from apps.articles.views import main_page, SearchResultsView, ArticleListView, articles_json, ArticleFormView

app_name = 'articles'

urlpatterns = [
    path('search/', main_page, name='main-page'),
    path('results/', SearchResultsView.as_view(), name='search-results'),
    path('json/', articles_json, name='json-artilce-list'),
    path('list/', ArticleListView.as_view(), name='article-list'),
    path('form/', ArticleFormView.as_view(), name='article-form')
]
