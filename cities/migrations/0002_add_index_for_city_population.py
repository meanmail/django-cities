# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='population',
            field=models.IntegerField(db_index=True),
        ),
    ]
