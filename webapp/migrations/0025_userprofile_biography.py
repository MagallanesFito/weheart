# Generated by Django 2.1.2 on 2018-12-06 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0024_remove_userprofile_biography'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='biography',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
