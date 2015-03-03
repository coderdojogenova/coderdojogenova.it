# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'Titolo')),
                ('content', models.TextField(verbose_name=b'Contenuto')),
                ('slug', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'Pubblicato il')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
