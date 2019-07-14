from django.shortcuts import render, redirect, reverse, HttpResponseRedirect, get_object_or_404
from .forms import loginForm
from django.contrib.auth import authenticate, login,logout
from .models import *


def home_view(request):
    form = loginForm(request.POST or None)
    context = {
        'form': form,
    }
    if request.user.is_authenticated:
        if request.user.is_staff == True:
            return HttpResponseRedirect(reverse('admin:index'))
        else:
            return redirect('musteri')

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if user.is_staff == True:
            return HttpResponseRedirect(reverse('admin:index'))
        else:
            return redirect('musteri')
    return render(request, 'home.html', context)


def listFilm(request):
    sinemalar = Sinemalar.objects.all()
    filmler = Filmler.objects.all()
    salonlar = Salonlar.objects.all()
    seanslar = Seanslar.objects.all()
    context = {
        'sinemalar': sinemalar,
        'salonlar': salonlar,
        'seanslar': seanslar,
        'filmler': filmler,
    }
    return render(request, 'normal.html', context)


def filmDetay(request, id):
    film = get_object_or_404(Filmler, id=id)
    seans = Seanslar.objects.all()
    list=[]
    for i in seans:
        if i.film_adi == film.film_adi:
            list.append((i.seans_zaman))
    return render(request, 'detay.html', {
        'film': film,
        'list': list,
    }

    )

def logoutAccount(request):
    logout(request)
    return redirect('home')
# Create your views here.
