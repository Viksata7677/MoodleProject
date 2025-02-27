# Generated by Django 5.1.3 on 2024-11-16 16:23

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworks', '0004_remove_homework_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='grade',
            field=models.DecimalField(blank=True, choices=[(Decimal('2.00'), '2.00'), (Decimal('3.00'), '3.00'), (Decimal('4.00'), '4.00'), (Decimal('5.00'), '5.00'), (Decimal('6.00'), '6.00')], decimal_places=2, max_digits=4, null=True),
        ),
    ]
