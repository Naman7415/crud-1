# Generated by Django 4.2 on 2023-12-08 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_remove_task_bust_author_bust'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='bust',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='photos.task'),
        ),
    ]
