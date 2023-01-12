# Generated by Django 4.1.4 on 2023-01-09 12:22

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=100)),
                ("slug", models.SlugField(null=True)),
                ("genre", models.CharField(max_length=30)),
                ("author", models.CharField(max_length=30)),
                ("isbn", models.IntegerField()),
                ("count", models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
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
                    "date_modified",
                    models.DateTimeField(
                        auto_now=True, verbose_name=django.contrib.auth.models.User
                    ),
                ),
                (
                    "follows",
                    models.ManyToManyField(
                        blank=True, related_name="followed_by", to="main.profile"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]