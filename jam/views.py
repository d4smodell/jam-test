from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .forms import UserRegisterForm, UserLoginForm
from .models import Band


class Home(ListView):
    model = Band
    template_name = 'jam/index.html'
    context_object_name = 'bands'
    paginate_by = 4


class SingleGenre(ListView):
    template_name = 'jam/single_genre.html'
    context_object_name = 'bands'

    def get_queryset(self):
        return Band.objects.filter(genre__slug=self.kwargs['slug'])


class SingleBand(DetailView):
    template_name = 'jam/single_band.html'
    context_object_name = 'band'
    model = Band


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration was successful')
            return redirect('login')
        else:
            messages.error(request, 'Something goes Wrong')
    else:
        form = UserRegisterForm()
    return render(request, 'jam/register.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'jam/login.html', {'form': form})
