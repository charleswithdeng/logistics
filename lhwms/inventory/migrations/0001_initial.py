# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-10-14 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stock_mark', models.CharField(max_length=16, null=True)),
                ('apply_cons_mark', models.CharField(db_index=True, max_length=16)),
                ('mat_mark', models.CharField(max_length=16)),
                ('pars', models.CharField(max_length=32)),
                ('wh_mark', models.CharField(max_length=16)),
                ('num', models.DecimalField(decimal_places=3, max_digits=12)),
                ('test_result', models.CharField(max_length=16)),
                ('is_visible', models.BooleanField(default=True)),
                ('is_enable', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
