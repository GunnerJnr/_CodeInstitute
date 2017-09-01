# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 11:45
from __future__ import unicode_literals

import accounts.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_stripe_id'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', accounts.models.AccountUserManager()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='subscription_end',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]