# Generated by Django 4.1.3 on 2022-11-14 14:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ad",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=60,
                        validators=[django.core.validators.MinLengthValidator(10)],
                    ),
                ),
                (
                    "price",
                    models.PositiveIntegerField(
                        default=0,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "description",
                    models.TextField(default="", max_length=300, null=True),
                ),
                ("is_published", models.BooleanField(default=False)),
                ("image", models.ImageField(null=True, upload_to="images/")),
            ],
            options={
                "verbose_name": "Объявление",
                "verbose_name_plural": "Объявления",
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="", max_length=50)),
                (
                    "slug",
                    models.SlugField(
                        max_length=10,
                        null=True,
                        unique=True,
                        validators=[django.core.validators.MinLengthValidator(5)],
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Selection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="Подборка", max_length=30)),
                ("ads", models.ManyToManyField(to="ads.ad")),
            ],
            options={
                "verbose_name": "Подборка",
                "verbose_name_plural": "Подборки",
            },
        ),
    ]
