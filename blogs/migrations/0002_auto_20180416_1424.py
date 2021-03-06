# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airticle',
            name='image',
            field=models.BinaryField(blank=True),
        ),
        migrations.AlterField(
            model_name='airticle',
            name='tag',
            field=models.ManyToManyField(blank=True, to='blogs.Tag'),
        ),
    ]
