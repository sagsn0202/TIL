from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import MovieModelForm
from django.contrib.auth.decorators import login_required


def index(request):
    movies = Movie.objects.all()
    return render(request, 'movie/list.html', {
        'movies': movies
    })


@login_required(login_url='/accounts/sign_in/')
def create(request):
    if request.method == 'POST':
        form = MovieModelForm(request.POST)
        if form.is_valid():
            # title = form.cleaned_data.get('title')
            # title_eng = form.cleaned_data.get('title_eng')
            # audience = form.cleaned_data.get('audience')
            # open_date = form.cleaned_data.get('open_date')
            # genre = form.cleaned_data.get('genre')
            # watch_grade = form.cleaned_data.get('watch_grade')
            # score = form.cleaned_data.get('score')
            # poster_url = form.cleaned_data.get('poster_url')
            # description = form.cleaned_data.get('description')
            #
            # Movie.objects.create(
            #     title=title,
            #     title_eng=title_eng,
            #     audience=audience,
            #     open_date=open_date,
            #     genre=genre,
            #     watch_grade=watch_grade,
            #     score=score,
            #     poster_url=poster_url,
            #     description=description,
            # )
            form.save()
            return redirect('movie:list')
    else:
        form = MovieModelForm()

    return render(request, 'movie/create.html', {'form': form})


def update(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = MovieModelForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie:detail', movie_id)
    else:
        form = MovieModelForm(instance=movie)
    return render(request, 'movie/update.html', {'form': form})
