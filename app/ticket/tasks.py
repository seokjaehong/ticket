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
    'get_ticket_information_save_KE',
    'get_ticket_information_save_OZ',
    'get_ticket_information_save_LJ',
    'get_ticket_information_save_ZE',
    'get_ticket_information_save_TW',
    'get_ticket_information_save_7C',
)
departure_date = datetime.date.today()
add_days = 10
edate = departure_date + datetime.timedelta(days=add_days)


def ticket_info_base(flight_company):
    start_time = time.time()

    for single_date in daterange(departure_date, edate):
        get_ticket_information_single_date(
            origin_place='GMP',
            destination_place='CJU',
            departure_date=single_date,
            flight_company=flight_company
        )
    print("---company code: {} , {}seconds ---".format(flight_company, (time.time() - start_time)))


@app.task()
def get_ticket_information_save_BX():
    ticket_info_base('BX')


@app.task()
def get_ticket_information_save_7C():
    ticket_info_base('7C')


@app.task()
def get_ticket_information_save_KE():
    ticket_info_base('KE')


@app.task()
def get_ticket_information_save_OZ():
    ticket_info_base('OZ')


@app.task()
def get_ticket_information_save_LJ():
    ticket_info_base('LJ')


@app.task()
def get_ticket_information_save_ZE():
    ticket_info_base('ZE')


@app.task()
def get_ticket_information_save_TW():
    ticket_info_base('TW')
