# Generated by Django 3.2.4 on 2021-07-02 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210702_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='details',
            field=models.TextField(blank=True, help_text='provide any additional details', null=True),
        ),
    ]