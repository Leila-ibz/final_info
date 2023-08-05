# Generated by Django 4.2.3 on 2023-08-05 22:26

import apps.posts.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('resumen', models.TextField()),
                ('contenido', models.TextField()),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='posts')),
                ('estado', models.BooleanField(default=True)),
                ('publicado', models.DateTimeField(default=django.utils.timezone.now)),
                ('avatar', models.ImageField(blank=True, default=apps.posts.models.default_avatar, null=True, upload_to=apps.posts.models.get_random_avatar_filename)),
                ('nickname', models.CharField(default='Sin Nickname', max_length=30)),
            ],
            options={
                'ordering': ('-publicado',),
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='posts.articulo')),
            ],
        ),
    ]
