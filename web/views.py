from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from . import models


# Create your views here.

def index(request, page=1):
    article_list = models.Article.objects.filter(is_active=True).order_by("-published")
    paginator = Paginator(article_list, 3)
    articles = paginator.get_page(page)
    return render(request, "web/index.html", {
        'latest_post': articles,
    })


def post_detail(request, slug):
    post = get_object_or_404(models.Article, slug=slug, is_active=True)
    return render(request, "web/post.html", {
        "post": post,
    })


def contact_us(request):
    return render(request, "web/contact.html")


def about_us(request):
    return render(request, "web/about.html")


def all_posts(request):
    return render(request, "web/posts.html", {
        "posts": models.Article.objects.filter(is_active=True).order_by("-published"),
    })
