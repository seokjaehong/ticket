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
    'get_ticket_information_save',
)


@app.task()
def get_ticket_information_save(single_date, flight_company):
    start_time = time.time()
    get_ticket_information_single_date(
        origin_place='GMP',
        destination_place='CJU',
        departure_date=single_date,
        flight_company=flight_company
    )
    print("---company code: {},{} , {}seconds ---".format(flight_company, str(single_date), (time.time() - start_time)))
