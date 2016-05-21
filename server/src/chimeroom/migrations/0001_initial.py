# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chimeRoom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('capacity', models.IntegerField()),
                ('floor', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('active', models.BooleanField()),
                ('white_board', models.BooleanField()),
                ('projector', models.BooleanField()),
                ('internet', models.BooleanField()),
                ('wi_fi', models.BooleanField()),
                ('intercom', models.BooleanField()),
                ('tele_conferencing', models.BooleanField()),
                ('video_conferencing', models.BooleanField()),
            ],
        ),
    ]
