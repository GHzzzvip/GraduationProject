# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-12-02 05:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VirtualJudge', '0002_contest_contest_problem_problem_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contest_problem',
            old_name='p_source',
            new_name='p_oj',
        ),
        migrations.RenameField(
            model_name='problem',
            old_name='p_source',
            new_name='p_oj',
        ),
        migrations.RenameField(
            model_name='status',
            old_name='p_source',
            new_name='p_oj',
        ),
    ]