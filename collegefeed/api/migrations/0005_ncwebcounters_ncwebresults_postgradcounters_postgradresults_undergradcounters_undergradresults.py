# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_mphilresults'),
    ]

    operations = [
        migrations.CreateModel(
            name='ncwebcounters',
            fields=[
                ('ncwebid', models.IntegerField(serialize=False, primary_key=True)),
                ('ncwebtitle', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ncwebresults',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('linkf', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='postgradcounters',
            fields=[
                ('postgradid', models.IntegerField(serialize=False, primary_key=True)),
                ('postgradtitle', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='postgradresults',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField()),
                ('linkf', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='undergradcounters',
            fields=[
                ('undergradid', models.IntegerField(serialize=False, primary_key=True)),
                ('udergradtitle', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='undergradresults',
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
