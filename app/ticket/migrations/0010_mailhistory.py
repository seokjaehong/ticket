# Generated by Django 2.0.3 on 2018-06-20 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0009_auto_20180619_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='생성시간')),
                ('mail_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.MailCondition')),
                ('ticket_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.TicketData')),
            ],
        ),
    ]