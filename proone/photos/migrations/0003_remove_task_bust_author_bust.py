# Generated by Django 4.2 on 2023-12-08 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='bust',
        ),
        migrations.AddField(
            model_name='author',
            name='bust',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='photos.task'),
            preserve_default=False,
        ),
    ]
