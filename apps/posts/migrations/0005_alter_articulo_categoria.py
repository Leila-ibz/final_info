# Generated by Django 4.2.3 on 2023-08-04 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_articulo_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='categoria',
            field=models.ForeignKey(default='Sin categoria', null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.categoria'),
        ),
    ]