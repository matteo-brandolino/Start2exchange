# Generated by Django 2.2.13 on 2020-06-30 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_profile_wallet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='wallet',
        ),
    ]
