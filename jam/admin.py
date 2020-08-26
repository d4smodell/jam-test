from django.contrib import admin
from .models import Band, Album, Song, Genre


class BandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('name',)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('name',)


class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('name',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {"slug": ("name",)}
    list_display_links = ('name',)


admin.site.register(Band, BandAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Genre, GenreAdmin)