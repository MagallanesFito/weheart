# Generated by Django 2.1.2 on 2018-12-06 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0023_auto_20181206_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='biography',
        ),
    ]
