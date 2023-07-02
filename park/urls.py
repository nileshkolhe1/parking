from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('book', views.book, name='book'),
    path('my-parkings', views.myParkings, name='my-parkings'),

    #
]