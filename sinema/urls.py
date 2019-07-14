from django.urls import path
from .views import *

urlpatterns = [
    path('musteri', listFilm,name='musteri'),
    path('<int:id>',filmDetay, name='detay'),
    path('logout',logoutAccount)
]
