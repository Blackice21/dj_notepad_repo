# Generated by Django 3.1.3 on 2020-11-15 18:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notepad', '0002_auto_20201115_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='label',
            field=models.CharField(choices=[('p', 'primary'), ('se', 'secondary'), ('d', 'danger'), ('s', 'success'), ('w', 'warning'), ('i', 'info'), ('d', 'dark'), ('l', 'light')], default='primary', max_length=2),
        ),
        migrations.AlterField(
            model_name='note',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 11, 15, 12, 7, 59, 815398)),
        ),
    ]
