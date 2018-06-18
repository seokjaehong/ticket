# Generated by Django 2.0.3 on 2018-05-24 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0004_auto_20180524_0528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticketdata',
            name='url_link',
        ),
        migrations.AlterField(
            model_name='ticketdata',
            name='arrival_datetime',
            field=models.CharField(max_length=10, verbose_name='도착시간'),
        ),
        migrations.AlterField(
            model_name='ticketdata',
            name='departure_datetime',
            field=models.CharField(max_length=10, verbose_name='출발시간'),
        ),
    ]
