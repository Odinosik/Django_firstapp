from django.http import HttpResponse
from django.http import Http404
from .models import Album
from django.shortcuts import render
from django.template import loader


def index(request):
    #Connect DB
    all_albums = Album.objects.all()
    return render(request,'music/index.html', {'all_albums' : all_albums})

def detail(request, album_id):

    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")

    return render(request, 'music/detail.html', {'album': album})

def favorite(request, album_id):
    return ""