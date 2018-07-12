import datetime
from crawler.utils import get_ticket_information_single_date, daterange
from config.celery import app
import time

# KE: 대한항공
# OZ: 아시아나
# 7C: 제주항공
# LJ: 진에어
# BX: 에어부산
# ZE: 이스타항공
# TW: 티웨이항공
__all__ = (
    'get_ticket_information_save_BX',
    # 'get_ticket_information_save_KE_1',
    # 'get_ticket_information_save_KE_2',
    'get_ticket_information_save_KE',
    'get_ticket_information_save_OZ',
    'get_ticket_information_save_LJ',
    'get_ticket_information_save_ZE',
    'get_ticket_information_save_TW',
    'get_ticket_information_save_7C',
)


def ticket_info_base(flight_company, single_date):
    start_time = time.time()
    get_ticket_information_single_date(
        origin_place='GMP',
        destination_place='CJU',
        departure_date=single_date,
        flight_company=flight_company
    )
    print("---company code: {},{} , {}seconds ---".format(flight_company, str(single_date), (time.time() - start_time)))


@app.task()
def get_ticket_information_save_BX(single_date):
    ticket_info_base('BX', single_date)


@app.task()
def get_ticket_information_save_7C(single_date):
    ticket_info_base('7C', single_date)


@app.task()
def get_ticket_information_save_OZ(single_date):
    ticket_info_base('OZ', single_date)


@app.task()
def get_ticket_information_save_LJ(single_date):
    ticket_info_base('LJ', single_date)


@app.task()
def get_ticket_information_save_ZE(single_date):
    ticket_info_base('ZE', single_date)


@app.task()
def get_ticket_information_save_TW(single_date):
    ticket_info_base('TW', single_date)


@app.task()
def get_ticket_information_save_KE(single_date):
    ticket_info_base('KE', single_date)

# @app.task()
# def get_ticket_information_save_KE_1():
#     start_time = time.time()
#     half_day = departure_date + datetime.timedelta(days=add_days / 2)
#     for single_date in daterange(departure_date, half_day):
#         get_ticket_information_single_date(
#             origin_place='GMP',
#             destination_place='CJU',
#             departure_date=single_date,
#             flight_company='KE'
#         )
#     print("---company code: {} , {}seconds ---".format('KE', (time.time() - start_time)))
#
# @app.task()
# def get_ticket_information_save_KE_2():
#     start_time = time.time()
#     half_day = departure_date + datetime.timedelta(days=add_days / 2)
#     for single_date in daterange(half_day, edate):
#         get_ticket_information_single_date(
#             origin_place='GMP',
#             destination_place='CJU',
#             departure_date=single_date,
#             flight_company='KE'
#         )
#     print("---company code: {} , {}seconds ---".format('KE', (time.time() - start_time)))
