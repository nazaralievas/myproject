from django.shortcuts import render, redirect
from .models import Movie
from .forms import CommentForm


def homepage(request):
    movies = Movie.objects.filter(is_published=True)
    return render(request, 'core/homepage.html', {'movies': movies})


def movie_detail(request, id):
    movie = Movie.objects.get(id=id, is_published=True)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()
            return redirect('movie_detail', id=movie.id)

    form = CommentForm()
    return render(request, 'core/movie_detail.html', {'movie': movie, 'form': form})


# ----------- регистрация, авторизация, logout -------------
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def register(request):
    context = {}

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
        context['form'] = form
    else:
        context['form'] = UserCreationForm()
    return render(request, 'core/register.html', context)


from django.contrib import auth
def login(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        context = {}
        if request.method == "POST":
            form = auth.forms.AuthenticationForm(request, request.POST)
            if form.is_valid():
                user = form.get_user()
                auth.login(request, user)
                return redirect('homepage')
            context['form'] = form
        context["form"] = auth.forms.AuthenticationForm()
        return render(request, 'core/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('homepage')
