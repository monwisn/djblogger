# Generated by Django 4.1.4 on 2023-01-05 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="count",
            field=models.IntegerField(null=True),
        ),
    ]
