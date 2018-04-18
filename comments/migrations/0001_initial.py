# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20180416_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone_num', models.CharField(max_length=11)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField()),
                ('airticle_id', models.ForeignKey(to='blogs.airticle')),
            ],
        ),
    ]
