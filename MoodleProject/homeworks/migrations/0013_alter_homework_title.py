# Generated by Django 5.1.3 on 2024-11-30 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworks', '0012_alter_homework_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
