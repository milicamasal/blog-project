# Generated by Django 3.1.2 on 2020-10-13 13:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_dat',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 13, 13, 38, 34, 333761, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 13, 13, 38, 34, 333410, tzinfo=utc)),
        ),
    ]
