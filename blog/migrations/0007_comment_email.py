# Generated by Django 3.1.4 on 2021-01-05 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210101_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default='peizhiliu168@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]
