# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-10-29 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incoming', '0004_incomingapply_accessory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomingapply',
            name='accessory',
            field=models.FileField(null=True, upload_to='incoming/'),
        ),
    ]
