# Generated by Django 3.1.4 on 2020-12-26 02:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20201226_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='lastupdate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
