# Generated by Django 2.2.13 on 2020-06-29 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200629_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ips',
            field=models.Field(default=[]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='subprofiles',
            field=models.Field(default={}),
        ),
    ]
