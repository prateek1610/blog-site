# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-04-03 16:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='author_name',
            new_name='name',
        ),
    ]