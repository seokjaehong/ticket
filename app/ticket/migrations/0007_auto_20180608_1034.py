# Generated by Django 2.0.3 on 2018-06-08 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0006_ticketdata_leftseat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticketdata',
            old_name='Leftseat',
            new_name='leftseat',
        ),
    ]