from django.contrib import admin

from .models import Movie, Actor, Director


@admin.action(description='Опубликовать')
def make_published(self, request, queryset):
    queryset.update(is_published=True)


@admin.action(description='Снять с публикации')
def make_unpublished(self, request, queryset):
    queryset.update(is_published=False)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')
    list_filter = ('is_published', 'year')
    search_fields = ('title', 'id', 'genres')
    actions = (make_published, make_unpublished)


@admin.register(Actor, Director)
class CastAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth')



