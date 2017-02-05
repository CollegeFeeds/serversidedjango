# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170205_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mphilresults',
            name='id',
            field=models.AutoField(default=1, serialize=False, primary_key=True),
        ),
    ]
