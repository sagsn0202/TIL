from django.shortcuts import render,redirect
from .models import Article


def index(request):
    return render(request, 'board/index.html')


def greeting(request, name, role):
    if role == 'admin':
        return render(request, 'board/greeting.html', {
            'role': 'Master User',
            'name': name,
        })
    else:
        return render(request, 'board/greeting.html', {
            'role': role,
            'name': name,
        })


def article_new(request):
    return render(request, 'board/new.html')


def article_create(request):
    article = Article()
    article.title = request.POST.get('input_title')
    article.content = request.POST.get('input_content')
    article.save()
    return redirect(f'/board/articles/{article.id}/')


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'board/list.html', {
        'articles': articles
    })


def article_detail(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'board/detail.html', {
        'article': article,
    })


def article_edit(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'board/edit.html', {
        'article': article,
    })


def article_update(request, id):
    article = Article.objects.get(id=id)
    article.title = request.POST.get('input_title')
    article.content = request.POST.get('input_content')
    article.save()
    return redirect(f'/board/articles/{article.id}/')


def article_delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('/board/articles/')
