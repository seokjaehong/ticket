# Generated by Django 2.0.3 on 2018-06-29 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_address', models.CharField(max_length=40, verbose_name='email address')),
                ('username', models.CharField(blank=True, max_length=30, null=True, verbose_name='사용자 이름')),
                ('departure_date', models.DateField(verbose_name='출발날짜')),
                ('origin_place', models.CharField(max_length=50, verbose_name='출발도시')),
                ('destination_place', models.CharField(max_length=50, verbose_name='도착도시')),
                ('user_max_price', models.IntegerField(verbose_name='최대가격')),
                ('ticket', models.ManyToManyField(to='ticket.TicketData')),
            ],
            options={
                'ordering': ('departure_date',),
            },
        ),
    ]
