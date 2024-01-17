# Generated by Django 4.2 on 2023-12-08 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_alter_author_bust'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='bust',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='email',
            field=models.EmailField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='task',
            name='img',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='task',
            name='password',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='phone',
            field=models.IntegerField(blank=True),
        ),
    ]
