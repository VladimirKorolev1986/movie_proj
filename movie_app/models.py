from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    director_email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_url(self):
        return reverse('movie-director', args=[self.id])


class DressingRoom(models.Model):
    floor = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return f'{self.floor},  {self.number}'


class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'

    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dressing = models.OneToOneField(DressingRoom, on_delete=models.SET_NULL, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)

    def __str__(self):
        if self.gender == self.MALE:
            return f'Актер - {self.first_name} {self.last_name} {self.gender}'
        else:
            return f'Актриса - {self.first_name} {self.last_name} {self.gender}'

    def get_url(self):
        return reverse('movie-actor', args=[self.id])


class Movie(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'
    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollar'),
        (RUB, 'Rubles'),
    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1000000, blank=True, validators=[MinValueValidator(1)])
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='R')
    slug = models.SlugField(default='', null=False, db_index=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='actor_movie')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('movie-detail', args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.rating}% - {self.budget}'
