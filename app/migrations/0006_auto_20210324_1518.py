# Generated by Django 2.2.10 on 2021-03-24 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210324_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rawfile',
            name='lon',
            field=models.FloatField(default=1),
        ),
    ]
