# Generated by Django 5.0.1 on 2024-01-22 10:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad_detil', '0001_initial'),
        ('advocate', '0004_tbl_adv_adv_description_tbl_adv_adv_experience_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_adv',
            name='Adv_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ad_detil.sub_category'),
        ),
    ]
