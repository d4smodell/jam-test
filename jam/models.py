from django.db import models
from django.urls import reverse_lazy


class Band(models.Model):
    slug = models.SlugField(max_length=120, verbose_name='url')
    name = models.CharField(max_length=120, verbose_name='Название')
    photo = models.ImageField(blank=True, upload_to='photos/')
    albums = models.ManyToManyField('Album', verbose_name='Альбомы')
    genre = models.ManyToManyField('Genre', verbose_name='Жанры')

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('band', kwargs={"slug": self.slug})


class Album(models.Model):
    slug = models.SlugField(max_length=120, verbose_name='url')
    name = models.CharField(max_length=120, verbose_name='Название Альбома')
    songs = models.ManyToManyField('Song', verbose_name='Песни')

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('album', kwargs={"slug": self.slug})


class Song(models.Model):
    slug = models.SlugField(max_length=120, verbose_name='url')
    name = models.CharField(max_length=120, verbose_name='Песня')

    class Meta:
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'

    def __str__(self):
        return self.name


class Genre(models.Model):
    slug = models.SlugField(max_length=120, verbose_name='url')
    name = models.CharField(max_length=120, verbose_name='Жанр')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('genre', kwargs={"slug": self.slug})
