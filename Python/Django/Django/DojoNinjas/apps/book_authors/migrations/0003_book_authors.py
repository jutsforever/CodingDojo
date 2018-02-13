# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-13 03:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0002_remove_book_author_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='_authors', to='book_authors.Author'),
        ),
    ]