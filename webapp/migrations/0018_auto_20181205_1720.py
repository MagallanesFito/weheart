# Generated by Django 2.1.2 on 2018-12-05 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0017_auto_20181202_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='biography',
            field=models.TextField(default="Hey there, I'm using weHeart to make some friends!", null=True),
        ),
    ]
