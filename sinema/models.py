from django.db import models
from django.db.models import CharField
from django_mysql.models import ListCharField


class Sinemalar(models.Model):
    sinema_adi = models.CharField(max_length=120)
    sinema_yeri = models.CharField(max_length=120)
    salon_sayisi = models.IntegerField()

    def __str__(self):
        return self.sinema_adi


class Filmler(models.Model):
    film_afis=models.ImageField(upload_to='static')
    film_adi = models.CharField(max_length=100)
    film_yil = models.DateField()
    film_aktor = models.CharField(max_length=120)
    film_aktris = models.CharField(max_length=120)
    film_yonetmen = models.CharField(max_length=120)
    film_dil = models.CharField(max_length=120)
    film_sure = models.TimeField()

    def __str__(self):
        return self.film_adi


class Salonlar(models.Model):
    sinema_adi = models.ForeignKey(Sinemalar, on_delete=models.CASCADE)
    salon_adi = models.CharField(max_length=60)
    salon_kapasite = models.IntegerField()
    ses_sistemi = models.CharField(max_length=120)

    def __str__(self):
        return self.salon_adi


MATINE = (
    ('Sabah', 'Sabah'),
    ('Ogle', 'Ogle'),
    ('Aksam', 'Aksam')
)


class Seanslar(models.Model):

    salon_adi = models.ForeignKey(Salonlar, on_delete=models.CASCADE)
    film_adi = models.ForeignKey(Filmler, on_delete=models.CASCADE)
    seans_zaman = models.CharField(max_length=100, choices=MATINE)
    def __str__(self):
        return self.seans_zaman


class Bilet(models.Model):
    bilet_tur = models.CharField(max_length=60)
    bilet_fiyat = models.DecimalField(max_digits=4, decimal_places=2)
    def __str__(self):
        return self.bilet_tur