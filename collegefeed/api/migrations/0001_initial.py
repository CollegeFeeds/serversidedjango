# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mphilcounters',
            fields=[
                ('mphilid', models.IntegerField(serialize=False, primary_key=True)),
                ('mphiltitle', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='mphilresults',
            fields=[
                ('id', models.AutoField(default=1, serialize=False, primary_key=True)),
                ('title', models.TextField()),
                ('linkf', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
