from django.contrib import admin
from .models import *
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

# Register your models here.




admin.site.site_header = 'Sinema Otomasyon Yönetimi'
AdminSite.login_template = 'home.html'
AdminSite.logout_template = 'home.html'
AdminSite.site_url = None


class sinemaAdmin(admin.ModelAdmin):
    list_display = [
        'sinema_adi',
        'sinema_yeri',
        'salon_sayisi'
    ]

    class Meta:
        model = Sinemalar


class filmAdmin(admin.ModelAdmin):
    list_display = [
        'film_adi',
        'film_yonetmen',
        'film_aktor',
        'film_aktris',
        'film_yil',
    ]

    class Meta:
        model = Filmler


class seansAdmin(admin.ModelAdmin):
    list_display = [
        'salon_adi',
        'film_adi',
        'seans_zaman',
    ]

    class Meta:
        model = Seanslar


class salonAdmin(admin.ModelAdmin):
    list_display = [
        'sinema_adi',
        'salon_adi',
        'salon_kapasite',
    ]

    class Meta:
        model = Salonlar


class biletAdmin(admin.ModelAdmin):
    list_display = [
        'bilet_tur',
        'bilet_fiyat',
    ]

    class Meta:
        model = Bilet


admin.site.register(Seanslar)
admin.site.register(Bilet)
admin.site.register(Salonlar)
admin.site.register(Sinemalar, sinemaAdmin)
admin.site.register(Filmler, filmAdmin)
