# Generated by Django 5.1.3 on 2024-11-16 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeworks', '0002_homework_image_url_alter_homework_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homework',
            name='owner',
        ),
    ]