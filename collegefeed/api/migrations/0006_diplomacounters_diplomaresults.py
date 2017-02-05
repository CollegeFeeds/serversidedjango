# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_ncwebcounters_ncwebresults_postgradcounters_postgradresults_undergradcounters_undergradresults'),
    ]

    operations = [
        migrations.CreateModel(
            name='diplomacounters',
            fields=[
                ('undergradid', models.IntegerField(serialize=False, primary_key=True)),
                ('udergradtitle', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='diplomaresults',
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
