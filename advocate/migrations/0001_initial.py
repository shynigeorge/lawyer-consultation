# Generated by Django 5.0.1 on 2024-01-19 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tbl_adv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Adv_fname', models.CharField(max_length=20)),
                ('Adv_lname', models.CharField(max_length=20)),
                ('Adv_email', models.EmailField(default='', max_length=254)),
                ('Adv_gen', models.CharField(default='', max_length=10)),
                ('Adv_dob', models.DateField()),
                ('Adv_ph', models.CharField(max_length=10)),
                ('Adv_spec', models.CharField(max_length=20)),
                ('Adv_state', models.CharField(default='', max_length=30)),
                ('Adv_city', models.CharField(max_length=10)),
                ('Adv_dist', models.CharField(max_length=30)),
                ('Adv_pin', models.CharField(max_length=10)),
                ('Adv_status', models.BooleanField()),
                ('Adv_pass', models.CharField(max_length=20)),
            ],
        ),
    ]
