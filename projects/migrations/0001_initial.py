# Generated by Django 3.1.4 on 2020-12-14 04:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('color', models.CharField(default='ffffff', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('url', models.URLField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('lastupdate', models.DateTimeField(default=datetime.datetime(2020, 12, 14, 4, 7, 16, 711531))),
                ('technology', models.ManyToManyField(to='projects.Technology')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='projects')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
    ]