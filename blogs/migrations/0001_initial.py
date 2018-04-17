# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='airticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
                ('image', models.BinaryField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='airticle',
            name='category',
            field=models.ForeignKey(to='blogs.Category'),
        ),
        migrations.AddField(
            model_name='airticle',
            name='tag',
            field=models.ManyToManyField(to='blogs.Tag'),
        ),
    ]
