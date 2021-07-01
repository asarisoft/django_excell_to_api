# Generated by Django 3.1.2 on 2021-06-27 07:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('serial_number', '0002_serialnumber_value'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reward', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='redeem',
            name='value',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='scan',
            name='serial_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='serial_number.serialnumber'),
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateField(auto_now_add=True)),
                ('type', models.CharField(choices=[('debit', 'Debit'), ('credit', 'Credit')], max_length=10, null=True)),
                ('value', models.IntegerField(default=0)),
                ('redeem', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='reward.redeem')),
                ('scan', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='reward.scan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]