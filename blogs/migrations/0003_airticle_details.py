# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20180416_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='airticle',
            name='details',
            field=models.TextField(default=''),
        ),
    ]
