# Generated by Django 4.1.7 on 2023-03-25 12:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuapp', '0003_alter_daymenu_day_alter_timemenu_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timemenu',
            name='start_time',
            field=models.TimeField(default=datetime.datetime(2023, 3, 25, 15, 54, 52, 219953)),
        ),
    ]
