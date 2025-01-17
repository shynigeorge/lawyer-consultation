# Generated by Django 5.0.1 on 2024-02-02 10:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_booking_customer_booking_date_booking_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='case',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='u',
        ),
        migrations.RemoveField(
            model_name='case',
            name='u',
        ),
        migrations.AddField(
            model_name='booking',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='payment',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='booking',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='customer.booking'),
        ),
        migrations.AddField(
            model_name='case',
            name='document',
            field=models.FileField(null=True, upload_to='case_details'),
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
