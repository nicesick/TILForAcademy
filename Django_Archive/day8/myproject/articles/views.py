from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def index(request):
    articles = Article.objects.all()

    context = {
        'articles' : articles
    }

    return render(request, 'index.html', context)

def show(request, id):
    articles = Article.objects.get(id=id)

    context = {
        'articles' : articles
    }

    return render(request, 'show.html', context)

def new(request):
    if request.method == 'POST':
        title = request.POST['title']
        contents = request.POST['contents']
        creator = request.POST['creator']

        article = Article()
        article.title = title
        article.contents = contents
        article.creator = creator

        article.save()

        return redirect('articles:show', article.id)
    
    else:
        return render(request, 'new.html')

def edit(request, id):
    if request.method == 'POST':
        article = Article.objects.get(id=id)

        title = request.POST['title']
        contents = request.POST['contents']
        creator = request.POST['creator']

        article.title = title
        article.contents = contents
        article.creator = creator

        article.save()

        return redirect('articles:show', article.id)

    else:
        articles = Article.objects.get(id=id)

        context = {
            'articles' : articles
        }

        return render(request, 'edit.html', context)

def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()

    return redirect('articles:index')