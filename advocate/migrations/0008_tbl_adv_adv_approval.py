# Generated by Django 5.0.1 on 2024-02-19 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocate', '0007_remove_tbl_adv_adv_spec'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_adv',
            name='Adv_approval',
            field=models.BooleanField(default=False),
        ),
    ]