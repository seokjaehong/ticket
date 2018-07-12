import datetime
from datetime import timedelta
from crawler.utils import get_ticket_information_single_date, daterange, parser_raw_value_to_datefield
from config.celery import app

__all__ = (
    'get_ticket_information_save_BX',
    'get_ticket_information_save_KE',
    'get_ticket_information_save_OZ',
    'get_ticket_information_save_LJ',
    'get_ticket_information_save_ZE',
    'get_ticket_information_save_TW',
    'get_ticket_information_save_7C',
)


# KE: 대한항공
# OZ: 아시아나
# 7C: 제주항공
# LJ: 진에어
# BX: 에어부산
# ZE: 이스타항공
# TW: 티웨이항공

def parser_string_to_datetime(raw_string):
    """
    '2018-08-01' => datetime(2018,8,1)
    :param raw_string:
    :return:
    """
    return datetime.date(*(int(s) for s in raw_string.split('-')))


@app.task()
def get_ticket_information_save_BX(origin_place, destination_place, departure_date):
    edate = parser_string_to_datetime(departure_date) + timedelta(days=1)
    for single_date in daterange(parser_string_to_datetime(departure_date), edate):
        get_ticket_information_single_date(
            origin_place=origin_place, destination_place=destination_place,
            departure_date=single_date,
            flight_company="BX",
        )


@app.task()
def get_ticket_information_save_7C(origin_place, destination_place, departure_date):
    edate = parser_string_to_datetime(departure_date) + timedelta(days=1)
    for single_date in daterange(parser_string_to_datetime(departure_date), edate):
        r = get_ticket_information_single_date(
            origin_place=origin_place,
            destination_place=destination_place,
            departure_date=single_date,
            flight_company="7C",
        )


@app.task()
def get_ticket_information_save_KE(origin_place, destination_place, departure_date):
    edate = parser_string_to_datetime(departure_date) + timedelta(days=1)
    for single_date in daterange(parser_string_to_datetime(departure_date), edate):
        r = get_ticket_information_single_date(
            origin_place=origin_place,
            destination_place=destination_place,
            departure_date=single_date,
            flight_company="KE",
        )


@app.task()
def get_ticket_information_save_OZ(origin_place, destination_place, departure_date):
    edate = parser_string_to_datetime(departure_date) + timedelta(days=1)
    for single_date in daterange(parser_string_to_datetime(departure_date), edate):
        r = get_ticket_information_single_date(
            origin_place=origin_place,
            destination_place=destination_place,
            departure_date=single_date,
            flight_company="OZ",
        )


@app.task()
def get_ticket_information_save_LJ(origin_place, destination_place, departure_date):
    edate = parser_string_to_datetime(departure_date) + timedelta(days=1)
    for single_date in daterange(parser_string_to_datetime(departure_date), edate):
        r = get_ticket_information_single_date(
            origin_place=origin_place,
            destination_place=destination_place,
            departure_date=single_date,
            flight_company="LJ",
        )


@app.task()
def get_ticket_information_save_ZE(origin_place, destination_place, departure_date):
    edate = parser_string_to_datetime(departure_date) + timedelta(days=1)
    for single_date in daterange(parser_string_to_datetime(departure_date), edate):
        r = get_ticket_information_single_date(
            origin_place=origin_place,
            destination_place=destination_place,
            departure_date=single_date,
            flight_company="ZE",
        )


@app.task()
def get_ticket_information_save_TW(origin_place, destination_place, departure_date):
    edate = parser_string_to_datetime(departure_date) + timedelta(days=1)
    for single_date in daterange(parser_string_to_datetime(departure_date), edate):
        r = get_ticket_information_single_date(
            origin_place=origin_place,
            destination_place=destination_place,
            departure_date=single_date,
            flight_company="TW",
        )
