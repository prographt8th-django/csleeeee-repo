# Generated by Django 4.1.7 on 2023-03-23 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prography', '0002_humanmodel_likes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HumanModel',
            new_name='Human',
        ),
    ]