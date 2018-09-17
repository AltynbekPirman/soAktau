# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def create_langs(apps, schema_editor):
    LANGS = [
        {'code': 'rus', 'name': 'russian'},
        {'code': 'kaz', 'name': 'kazakh'}
    ]

    Language = apps.get_model("main", "Language")

    for lang in LANGS:
        Language.objects.create(code=lang['code'], name=lang['name'])


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_langs),
    ]
