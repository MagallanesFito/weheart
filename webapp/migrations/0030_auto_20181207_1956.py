# Generated by Django 2.1.2 on 2018-12-07 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0029_userprofile_cover_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='biography',
            field=models.TextField(max_length=130),
        ),
    ]