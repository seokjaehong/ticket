import os
import sys
from datetime import datetime
from re import sub

from selenium import webdriver

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django

django.setup()



class TicketDetailData():
    def get_flight_time_from_webpage(self, obj):
        time_info = obj.find_element_by_class_name('flight-module').find_element_by_class_name(
            'custom-primary-padding').text
        return time_info

    def get_flight_price_from_webpage(self, obj):
        price_raw = obj.find_element_by_class_name('grid-container').find_element_by_class_name(
            'all-col-shrink').find_element_by_class_name('primary-content')
        price_info = int(sub(r'[^\d.]', '', price_raw.text))

        return price_info

    def get_ticket_information(self):
        driver = webdriver.Chrome('chromedriver')

        departure_date = '2018.05.17'
        arrival_date = '2018.05.19'
        departure_city = 'SEL'
        arrival_city = "PUS"

        url = "https://www.expedia.co.kr/Flights-Search?flight-type=on" \
              "&starDate=" + departure_date + \
              "&endDate=" + arrival_date + \
              "&_xpid=11905%7C1" \
              "&mode=search" \
              "&trip=roundtrip" \
              "&leg1=from%3A%EC%84%9C%EC%9A%B8%2C+%ED%95%9C%EA%B5%AD+%28" \
              + departure_city + "-%EB%AA%A8%EB%93%A0+%EA%B3%B5%ED%95%AD%29%2Cto%3A%EB%B6%80%EC%82%B0%2C+%ED%95%9C%EA%B5%AD+%28" \
              + arrival_city + "-%EA%B9%80%ED%95%B4%EA%B5%AD%EC%A0%9C%EA%B3%B5%ED%95%AD%29%2Cdeparture%3A" \
              + departure_date + "TANYT&leg2=from%3A%EB%B6%80%EC%82%B0%2C+%ED%95%9C%EA%B5%AD+%28" \
              + arrival_city + "-%EA%B9%80%ED%95%B4%EA%B5%AD%EC%A0%9C%EA%B3%B5%ED%95%AD%29%2Cto%3A%EC%84%9C%EC%9A%B8%2C+%ED%95%9C%EA%B5%AD+%28" \
              + departure_city + "-%EB%AA%A8%EB%93%A0+%EA%B3%B5%ED%95%AD%29%2Cdeparture%3A" \
              + arrival_date + "TANYT&passengers=children%3A0%2Cadults%3A1%2Cseniors%3A0%2Cinfantinlap%3AY"

        driver.get(url)
        driver.implicitly_wait(5)

        flight_informations = driver.find_elements_by_id('flightModuleList')
        result = []

        for flight in flight_informations:
            departure_time = self.get_flight_time_from_webpage(flight)
            departure_price = self.get_flight_price_from_webpage(flight)

            flight.find_element_by_class_name('grid-container').find_element_by_class_name(
                'all-col-shrink').find_element_by_class_name('standard-col-l-margin').click()
            driver.implicitly_wait(5)

            arrival_time = self.get_flight_time_from_webpage(flight)
            arrival_price = self.get_flight_price_from_webpage(flight)

        new_departure_date = datetime.strftime(datetime.strptime(departure_date,'%Y.%m.%d'),'%Y-%m-%d')

        new_arrival_date = datetime.strftime(datetime.strptime(arrival_date,'%Y.%m.%d'),'%Y-%m-%d')
        # new_arrival_date   = datetime.strftime(datetime.strftime(arrival_date,'%Y.%m.%d'),'%Y-%m-%d')

        result.append({
            'goreturn': '1',
            'departure_date': new_departure_date,
            'departure_duration': departure_time,
            'country': 'Korea',
            'departure_city': departure_city,
            'arrival_city': arrival_city,
            'flight_company': '대한항공',
            'ticket_price': departure_price,
            'currency': 'test',
            'fee_policy': 'test',
            'data_source': 'expedia',
            'url_link': 'test',
        })
        result.append({
            'goreturn': '2',
            'departure_date': new_arrival_date,
            'departure_duration': arrival_time,
            'country': 'Korea',
            'departure_city': arrival_city,
            'arrival_city': departure_city,
            'flight_company': '대한항공',
            'ticket_price': arrival_price,
            'currency': 'test',
            'fee_policy': 'test',
            'data_source': 'expedia',
            'url_link': 'test',

        })

        return result


if __name__ == '__main__':
    from ticket.models import TicketData

    crawler = TicketDetailData()

    ticket_datas = crawler.get_ticket_information()

    for ticket_data in ticket_datas:
        # 도시, 회사정보 저장
        city, _ = TicketData.objects.get_or_create(
            goreturn=ticket_data['goreturn'],
            departure_date=ticket_data['departure_date'],
            departure_duration=ticket_data['departure_duration'],
            country='Korea',
            departure_city=ticket_data['departure_city'],
            arrival_city=ticket_data['arrival_city'],
            flight_company='대한항공',
            ticket_price=ticket_data['ticket_price'],
            currency='test',
            fee_policy='test',
            data_source='expedia',
            # url_link='test',
        )
