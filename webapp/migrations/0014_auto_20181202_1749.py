# Generated by Django 2.1.2 on 2018-12-02 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0013_auto_20181202_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='default.jpg', upload_to='profile_picture'),
        ),
    ]
