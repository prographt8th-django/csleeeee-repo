# Generated by Django 4.1.7 on 2023-03-23 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prography', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='humanmodel',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]