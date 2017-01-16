# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import xmodule_django.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseAggregatedMetaData',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('id', xmodule_django.models.CourseKeyField(max_length=255, serialize=False, primary_key=True, db_index=True)),
                ('total_modules', models.IntegerField(default=0)),
                ('total_assessments', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
