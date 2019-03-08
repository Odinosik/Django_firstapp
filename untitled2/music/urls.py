from django.urls import path
from django.conf.urls import include, url
from . import views


urlpatterns = [
    path('', views.index, name='index'),

    #/music/


    path('<int:album_id>/', views.detail, name='detail'),


    #/album_id/ favorite

    path('<int:album_id>/favorite/',views.favorite ,name='favorite')
]
