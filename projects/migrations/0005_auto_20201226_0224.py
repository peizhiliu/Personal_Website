# Generated by Django 3.1.4 on 2020-12-26 02:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20201215_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='lastupdate',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 26, 2, 24, 47, 791268, tzinfo=utc)),
        ),
    ]
