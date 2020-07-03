# Generated by Django 2.2.13 on 2020-06-29 20:07

import app.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', djongo.models.fields.EmbeddedField(model_container=app.models.Profile, null=True)),
                ('price', models.FloatField(default=0)),
                ('quantity', models.FloatField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='ips',
            field=models.Field(default=[]),
        ),
    ]
