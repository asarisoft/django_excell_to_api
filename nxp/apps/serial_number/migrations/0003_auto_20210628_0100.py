# Generated by Django 3.1.2 on 2021-06-28 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serial_number', '0002_serialnumber_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serialnumber',
            name='value',
            field=models.IntegerField(default=400),
        ),
    ]