# Generated by Django 3.2.7 on 2021-09-18 07:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_postmodel_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 18, 7, 20, 3, 243616, tzinfo=utc), verbose_name='زمان انتشار'),
        ),
    ]
