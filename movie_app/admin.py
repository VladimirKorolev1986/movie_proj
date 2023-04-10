from django.contrib import admin
from .models import Movie


# Register your models here.

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'year', 'budget', 'rating_status']
    list_editable = ['rating', 'year', 'budget']
    ordering = ['rating']
    list_per_page = 2

    def rating_status(self, mov):
        if mov.rating < 60:
            return 'Зачем это смотреть?'
        if mov.rating < 60:
            return 'Разок можно глянуть'
        if mov.rating <= 85:
            return 'Зачет'
        else:
            return 'Топчик'
