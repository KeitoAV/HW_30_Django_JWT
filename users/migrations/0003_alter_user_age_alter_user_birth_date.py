# Generated by Django 4.1.3 on 2022-11-14 14:41

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_age"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="age",
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="birth_date",
            field=models.DateField(
                blank=True, null=True, validators=[users.validators.check_min_age]
            ),
        ),
    ]
