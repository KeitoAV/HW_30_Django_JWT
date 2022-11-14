from django.core.validators import EmailValidator, RegexValidator
from django.contrib.auth.models import AbstractUser
from django.db import models

from users.validators import check_min_age


class Location(models.Model):
    name = models.CharField(max_length=60, default='')
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class User(AbstractUser):
    MEMBER = "member"
    MODERATOR = "moderator"
    ADMIN = "admin"
    ROLES = [(MEMBER, "Пользователь"), (MODERATOR, "Модератор"), (ADMIN, "Администратор")]

    first_name = models.CharField(verbose_name="Имя", max_length=100, null=True)
    last_name = models.CharField(verbose_name="Фамилия", max_length=150, null=True)
    username = models.CharField(verbose_name="Логин", max_length=20, unique=True)
    password = models.CharField(verbose_name="Пароль", max_length=200)
    role = models.CharField(max_length=10, choices=ROLES, default='member')
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    location = models.ManyToManyField(Location)

    birth_date = models.DateField(blank=True, null=True, validators=[check_min_age])
    email = models.CharField(
        max_length=254,
        null=True,
        unique=True,
        validators=[EmailValidator(),
                    RegexValidator(regex=r"(?:rambler\.ru)", inverse_match=True, message='Домен Рамблера запрещен.')]
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
