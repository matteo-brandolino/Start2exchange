# Generated by Django 2.2.13 on 2020-06-30 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20200630_2030'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='_id',
            new_name='profile',
        ),
    ]
