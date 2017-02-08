# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_diplomacounters_diplomaresults'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diplomacounters',
            old_name='undergradid',
            new_name='diplomaid',
        ),
        migrations.RenameField(
            model_name='diplomacounters',
            old_name='udergradtitle',
            new_name='diplomatitle',
        ),
        migrations.RenameField(
            model_name='undergradcounters',
            old_name='udergradtitle',
            new_name='undergradtitle',
        ),
    ]
