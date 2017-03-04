# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 13:27
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailusers.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailusers', '0005_make_related_name_wagtail_specific'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=wagtail.wagtailusers.models.upload_avatar_to, verbose_name='Upload your custom avatar'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='avatar_choice',
            field=models.CharField(choices=[('Default', 'Default'), ('Custom', 'Custom'), ('Gravatar', 'Gravatar')], default='Gravatar', max_length=10, verbose_name='Select avatar backend'),
        ),
    ]