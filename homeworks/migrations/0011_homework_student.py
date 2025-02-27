# Generated by Django 5.1.3 on 2024-11-19 18:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_customuser_role'),
        ('homeworks', '0010_alter_homework_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='homework', to='accounts.student'),
            preserve_default=False,
        ),
    ]
