# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_mphilcounters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mphilresults',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
