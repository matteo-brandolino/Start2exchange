# Generated by Django 2.2.13 on 2020-06-30 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_auto_20200630_2236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='_id',
        ),
    ]
