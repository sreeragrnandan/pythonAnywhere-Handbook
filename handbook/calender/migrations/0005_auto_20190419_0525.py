# Generated by Django 2.1.2 on 2019-04-18 23:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calender', '0004_auto_20190419_0503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventinfo',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
