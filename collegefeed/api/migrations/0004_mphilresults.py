# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_delete_mphilresults'),
    ]

    operations = [
        migrations.CreateModel(
            name='mphilresults',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('linkf', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
