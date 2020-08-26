# Generated by Django 3.1 on 2020-08-25 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jam', '0002_auto_20200825_1336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='bands',
        ),
        migrations.AddField(
            model_name='band',
            name='genre',
            field=models.ManyToManyField(to='jam.Genre', verbose_name='Жанры'),
        ),
        migrations.AddField(
            model_name='band',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/'),
        ),
    ]