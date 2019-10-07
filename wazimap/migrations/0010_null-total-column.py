# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-10-23 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wazimap', '0009_datatables'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fieldtable',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='simpletable',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='simpletable',
            name='total_column',
            field=models.CharField(blank=True, help_text=b"Name of the column that contains the total value of all the columns in the row. Wazimap usse this to express column values as a percentage. If this is not set, the table doesn't have the concept of a total and only absolute values (not percentages) will be displayed.", max_length=50, null=True),
        ),
    ]