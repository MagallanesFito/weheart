# Generated by Django 2.1.2 on 2018-11-30 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20181130_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cover_picture',
            field=models.ImageField(blank=True, upload_to='cover_picture'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='profile_picture'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='biography',
            field=models.TextField(null=True),
        ),
    ]
