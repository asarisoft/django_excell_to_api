# Generated by Django 3.1.2 on 2021-05-26 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('serial_number', '0004_auto_20210525_2259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serialnumber',
            name='generated_count',
        ),
    ]
