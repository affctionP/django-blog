# Generated by Django 3.2.7 on 2021-09-18 07:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 18, 7, 19, 31, 792901, tzinfo=utc), verbose_name='زمان انتشار'),
        ),
    ]
