# Generated by Django 3.2.4 on 2021-06-07 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_alter_profile_middle_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="middle_name",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
