# Generated by Django 4.2 on 2023-12-08 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0012_rename_email_task_emailcopy_rename_img_task_imgcopy_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
