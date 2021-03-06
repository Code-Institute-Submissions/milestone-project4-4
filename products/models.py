from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Game(models.Model):
    """Model migration for game product"""
    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Indie', 'Indie'),
        ('Fantasy', 'Fantasy'),
        ('RPG', 'RPG'),
        ('Simulator', 'Simulator'),
        ('Shooter', 'Shooter'),
        ('Sports and racing', 'Sports and racing'),
        ('Strategy', 'Strategy')
    ]

    WORKS_ON_CHOICES = [
        ('Windows', 'Windows'),
        ('Linux', 'Linux'),
        ('Mac', 'Mac'),
    ]

    PEGI_RATING_CHOICES = [
        ('3', '3'),
        ('7', '7'),
        ('12', '12'),
        ('16', '16'),
        ('18', '18'),
    ]

    name = models.CharField(max_length=120, default='')
    description = models.TextField(default='Description missing.')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='images')
    genre = models.CharField(max_length=17, choices=GENRE_CHOICES, blank=False)
    genre_two = models.CharField(max_length=17, choices=GENRE_CHOICES, blank=True)
    genre_three = models.CharField(max_length=17, choices=GENRE_CHOICES, blank=True)
    works_on = models.CharField(max_length=7, choices=WORKS_ON_CHOICES, blank=False)
    works_on_two = models.CharField(max_length=7, choices=WORKS_ON_CHOICES, blank=True)
    works_on_three = models.CharField(max_length=7, choices=WORKS_ON_CHOICES, blank=True)
    release_date = models.DateField()
    company = models.CharField(max_length=30)
    pegi_rating = models.CharField(max_length=2, choices=PEGI_RATING_CHOICES, blank=True)
    single_player = models.BooleanField(null=True)
    multiplayer = models.BooleanField(null=True)
    discount = models.PositiveSmallIntegerField(blank=True, null=True)
    sale_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, default=0)
    banner_image = models.ImageField(upload_to='images', blank=True)
    video_url = models.URLField(max_length=200, blank=False)

    def __str__(self):
        return self.name


class Review(models.Model):
    """Model migration design for reviews"""

    title = models.CharField(max_length=40, null=False)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    rating = models.IntegerField(blank=False)
    game = models.ForeignKey(Game, related_name="reviews",
                             on_delete=models.CASCADE,
                             related_query_name="review", null=True)
    user = models.ForeignKey(User, related_name="reviews",
                             on_delete=models.CASCADE,
                             related_query_name="review", null=True)

    class meta:
        unique_together = ('game', 'user')

    def __str__(self):
        return self.title
