# Generated by Django 3.1.2 on 2020-10-13 13:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201013_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_dat',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 13, 13, 50, 38, 328402, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 13, 13, 50, 38, 328039, tzinfo=utc)),
        ),
    ]
