# Generated by Django 4.2 on 2023-12-07 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('password', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('img', models.ImageField(upload_to='images')),
            ],
        ),
    ]
