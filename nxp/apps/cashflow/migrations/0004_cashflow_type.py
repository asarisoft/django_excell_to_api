# Generated by Django 3.2 on 2022-05-24 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashflow', '0003_alter_cashflow_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashflow',
            name='type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
