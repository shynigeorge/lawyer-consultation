# Generated by Django 5.0.1 on 2024-02-29 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advocate', '0008_tbl_adv_adv_approval'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_adv',
            name='Adv_join_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
