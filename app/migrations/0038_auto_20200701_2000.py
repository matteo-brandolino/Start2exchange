# Generated by Django 2.2.13 on 2020-07-01 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0037_auto_20200701_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('ips', models.Field(default=[])),
                ('subprofiles', models.Field(default={})),
                ('wallet', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='profile',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.Profile'),
        ),
    ]
