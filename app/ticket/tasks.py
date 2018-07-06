import datetime
from datetime import timedelta
from crawler.utils import get_ticket_information_single_date, daterange
from config.celery import app

__all__ = (
    'get_ticket_information_save',
)


@app.task(bind=True)
def get_ticket_information_save(self,origin_place, destination_place, departure_date):
    datetime_departure_date = datetime.date(*(int(s) for s in departure_date.split('-')))

    edate = datetime_departure_date + timedelta(days=10)
    for single_date in daterange(datetime_departure_date, edate):
        get_ticket_information_single_date(
            origin_place=origin_place,
            destination_place=destination_place,
            departure_date=single_date
            )
    return f'{origin_place}-{destination_place}:{departure_date} save...'
