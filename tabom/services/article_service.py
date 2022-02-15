from tabom.models import Article
from django.db.models import QuerySet
from django.core.paginator import Paginator, Page


def get_an_article(article_id: int) -> Article:
    article = Article.objects.filter(id=article_id).get()
    return article;
        

def get_article_list(offset: int, limit: int) -> QuerySet[Article]:
    return Article.objects.order_by("-id")[offset : offset + limit]

def get_article_page(page: int, limit: int) -> Page:
    return Paginator(Article.objects.order_by("-id"), limit).page(page)
