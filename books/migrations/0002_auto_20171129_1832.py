# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 18:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='book_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='volume_num',
            new_name='volume',
        ),
    ]
