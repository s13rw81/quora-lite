# Generated by Django 3.2.4 on 2021-06-09 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_answer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="details",
            field=models.TextField(help_text="add any additional details"),
        ),
    ]
