from django.db import models

from django.urls import reverse


class Actor(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Полное имя'
    )
    date_of_birth = models.DateField(
        blank=False,
        null=True,
        verbose_name='Дата рождения'
    )
    place = models.CharField(
        max_length=50,
        null=True,
        verbose_name='Страна'
    )
    personal_foto = models.ImageField(
        upload_to='actors/',
        verbose_name='Фотография'
    )
    biography = models.CharField(
        max_length=500,
        verbose_name='Биография'
    )
    masterpiece = models.CharField(
        max_length=500,
        null=True,
        verbose_name='Лучшие работы'
    )
    award_link = models.URLField(
        'Достижения',
        max_length=500,
        null=True,
        default=None
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('actor_detail', kwargs={"slug": self.name})

    class Meta:
        db_table = 'actors'
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'


class Director(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Полное имя'
    )
    date_of_birth = models.DateField(
        blank=False,
        null=True,
        verbose_name='Дата рождения'
    )
    place = models.CharField(
        max_length=50,
        null=True,
        verbose_name='Страна'
    )
    personal_foto = models.ImageField(
        upload_to='director/',
        verbose_name='Фотография'
    )
    biography = models.CharField(
        max_length=500,
        verbose_name='Биография'
    )
    masterpiece = models.CharField(
        max_length=500,
        null=True,
        verbose_name='Лучшие работы'
    )
    award_link = models.URLField(
        'Достижения',
        max_length=500,
        null=True,
        default=None
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('director_detail', kwargs={"slug": self.name})

    class Meta:
        db_table = 'director'
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'


class Movie(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Название фильма'
    )
    tagline = models.CharField(
        max_length=100,
        verbose_name='Заголовок фильма'
    )
    description = models.TextField(
        max_length=1000,
        verbose_name='Описание'
    )
    poster = models.ImageField(
        upload_to='movies/',
        verbose_name='Постер'
    )
    year = models.DateField(
        verbose_name='Дата выхода фильма'
    )
    rating = models.FloatField(
        blank=True,
        null=True,
        verbose_name='Оценка'
    )
    metascore = models.IntegerField(
        blank=True,
        null=False,
        default=None,
        verbose_name='Рейтинг Metascore')
    country = models.CharField(
        'Страна',
        max_length=30
    )
    budget = models.PositiveIntegerField(
        'Бюджет',
        default=0,
        help_text='указывать сумму в долларах'
    )
    fess_in_world = models.PositiveIntegerField(
        'Сборы в мире',
        default=0,
        help_text='указывать сумму в долларах'
    )
    duration = models.IntegerField(
        blank=True,
        null=True,
        verbose_name='Продолжительность',
        help_text='указывать в минутах'
    )
    genres = models.CharField(
        max_length=27,
        verbose_name='Жанр')
    directors = models.ManyToManyField(
        Director,
        verbose_name='режиссер',
        related_name='film_director'
    )
    actors = models.ManyToManyField(
        Actor,
        verbose_name='актеры',
        related_name='film_actor'
    )
    url = models.SlugField(
        unique=True,
        verbose_name='URL'
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='Опубликован'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'slug': self.url})

    class Meta:
        db_table = 'movies'
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['title', '-year']


class Reviews(models.Model):
    # Отзывы
    name = models.CharField('Имя', max_length=100)
    email = models.EmailField()
    text = models.TextField('Сообщение', max_length=5000)
    movie = models.ForeignKey(Movie, verbose_name='фильм', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'