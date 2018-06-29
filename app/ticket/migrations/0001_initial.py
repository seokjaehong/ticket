# Generated by Django 2.0.3 on 2018-06-29 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TicketData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_place', models.CharField(max_length=50, verbose_name='출발도시')),
                ('destination_place', models.CharField(max_length=50, verbose_name='도착도시')),
                ('is_direct', models.BooleanField(default=False, verbose_name='경유여부')),
                ('way_point', models.CharField(max_length=50, verbose_name='경유지')),
                ('way_point_duration', models.CharField(max_length=10, verbose_name='경유시간')),
                ('ticket_price', models.IntegerField(verbose_name='가격')),
                ('departure_date', models.DateField(verbose_name='출발날짜')),
                ('departure_datetime', models.CharField(max_length=10, verbose_name='출발시간')),
                ('arrival_date', models.DateField(verbose_name='도착날짜')),
                ('arrival_datetime', models.CharField(max_length=10, verbose_name='도착시간')),
                ('flight_time', models.CharField(max_length=100, verbose_name='총소요시간')),
                ('leftseat', models.CharField(blank=True, max_length=30, verbose_name='잔여좌석')),
                ('flight_company', models.CharField(max_length=20, verbose_name='항공사명')),
                ('currency', models.CharField(blank=True, max_length=10, verbose_name='환율')),
                ('data_source', models.CharField(max_length=30, verbose_name='데이터 출처')),
                ('is_delete', models.BooleanField(default=False, verbose_name='삭제데이터여부')),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='생성시간')),
                ('modify_datetime', models.DateTimeField(auto_now_add=True, verbose_name='수정시간')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='설명')),
            ],
            options={
                'ordering': ('departure_date', 'departure_datetime'),
            },
        ),
    ]
