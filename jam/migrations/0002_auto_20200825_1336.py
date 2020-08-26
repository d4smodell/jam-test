# Generated by Django 3.1 on 2020-08-25 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jam', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'verbose_name': 'Альбом', 'verbose_name_plural': 'Альбомы'},
        ),
        migrations.AlterModelOptions(
            name='band',
            options={'verbose_name': 'Исполнитель', 'verbose_name_plural': 'Исполнители'},
        ),
        migrations.AlterModelOptions(
            name='song',
            options={'verbose_name': 'Песня', 'verbose_name_plural': 'Песни'},
        ),
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Название Альбома'),
        ),
        migrations.AlterField(
            model_name='album',
            name='slug',
            field=models.SlugField(max_length=120, verbose_name='url'),
        ),
        migrations.AlterField(
            model_name='album',
            name='songs',
            field=models.ManyToManyField(to='jam.Song', verbose_name='Песни'),
        ),
        migrations.AlterField(
            model_name='band',
            name='albums',
            field=models.ManyToManyField(to='jam.Album', verbose_name='Альбомы'),
        ),
        migrations.AlterField(
            model_name='band',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='band',
            name='slug',
            field=models.SlugField(max_length=120, verbose_name='url'),
        ),
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Песня'),
        ),
        migrations.AlterField(
            model_name='song',
            name='slug',
            field=models.SlugField(max_length=120, verbose_name='url'),
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=120, verbose_name='url')),
                ('name', models.CharField(max_length=120, verbose_name='Жанр')),
                ('bands', models.ManyToManyField(to='jam.Band', verbose_name='Группы')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
    ]
