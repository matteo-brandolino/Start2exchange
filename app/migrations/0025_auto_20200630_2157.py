# Generated by Django 2.2.13 on 2020-06-30 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20200630_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
