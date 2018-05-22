import os
import sys
from datetime import datetime
from datetime import timedelta
from re import sub

from selenium import webdriver

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django

django.setup()


class TicketDetailData():
    # def get_flight_time_from_webpage(self, obj):
    #     time_info = obj.find_element_by_class_name('flight-module').find_element_by_class_name(
    #         'custom-primary-padding').text
    #     print(time_info)
    #     return time_info
    #
    # def get_flight_price_from_webpage(self, obj):
    #     price_raw = obj.find_element_by_class_name('grid-container').find_element_by_class_name(
    #         'all-col-shrink').find_element_by_class_name('primary-content')
    #     price_info = int(sub(r'[^\d.]', '', price_raw.text))
    #     print(price_info)
    #     return price_info
    departure_date = '2018.05.26'

    def get_ticket_information(self):
        driver = webdriver.Chrome('chromedriver')

        origin_place = 'ICN'
        destination_place = "ROM"
        url = "https://www.expedia.co.kr/Flights-Search?flight-type=on&starDate=" \
              + self.departure_date + "&_xpid=11905%7C1&mode=search&trip=oneway&leg1=from%3A%EC%84%9C%EC%9A%B8%2C+%ED%95%9C%EA%B5%AD+%28" \
              + origin_place + "-%EC%9D%B8%EC%B2%9C%EA%B5%AD%EC%A0%9C%EA%B3%B5%ED%95%AD%29%2Cto%3A%EB%A1%9C%EB%A7%88%2C+%EC%9D%B4%ED%83%88%EB%A6%AC%EC%95%84+%28" \
              + destination_place + "-%EB%AA%A8%EB%93%A0+%EA%B3%B5%ED%95%AD%29%2Cdeparture%3A" \
              + self.departure_date + "TANYT&passengers=children%3A0%2Cadults%3A1%2Cseniors%3A0%2Cinfantinlap%3AY"
        # departure_date = '2018.05.25'
        # arrival_date = '2018.06.01'
        # departure_city = 'ICN'
        # arrival_city = "PUS"
        #
        # url = "https://www.expedia.co.kr/Flights-Search?flight-type=on" \
        #       "&starDate=" + departure_date + \
        #       "&endDate=" + arrival_date + \
        #       "&_xpid=11905%7C1" \
        #       "&mode=search" \
        #       "&trip=roundtrip" \
        #       "&leg1=from%3A%EC%84%9C%EC%9A%B8%2C+%ED%95%9C%EA%B5%AD+%28" \
        #       + departure_city + "-%EB%AA%A8%EB%93%A0+%EA%B3%B5%ED%95%AD%29%2Cto%3A%EB%B6%80%EC%82%B0%2C+%ED%95%9C%EA%B5%AD+%28" \
        #       + arrival_city + "-%EA%B9%80%ED%95%B4%EA%B5%AD%EC%A0%9C%EA%B3%B5%ED%95%AD%29%2Cdeparture%3A" \
        #       + departure_date + "TANYT&leg2=from%3A%EB%B6%80%EC%82%B0%2C+%ED%95%9C%EA%B5%AD+%28" \
        #       + arrival_city + "-%EA%B9%80%ED%95%B4%EA%B5%AD%EC%A0%9C%EA%B3%B5%ED%95%AD%29%2Cto%3A%EC%84%9C%EC%9A%B8%2C+%ED%95%9C%EA%B5%AD+%28" \
        #       + departure_city + "-%EB%AA%A8%EB%93%A0+%EA%B3%B5%ED%95%AD%29%2Cdeparture%3A" \
        #       + arrival_date + "TANYT&passengers=children%3A0%2Cadults%3A1%2Cseniors%3A0%2Cinfantinlap%3AY"

        driver.get(url)
        driver.implicitly_wait(3)

        # flight_informations = driver.find_elements_by_id('flight-listing-container')
        flight_informations = driver.find_elements_by_class_name('flight-module')

        result = []
        i = 0
        # new_departure_date = datetime.strftime(datetime.strptime(self.departure_date, '%Y.%m.%d'), '%Y-%m-%d')
        new_departure_date = datetime.strptime(self.departure_date,'%Y.%m.%d')

        for flight in flight_informations:

            flight_info = flight.find_element_by_css_selector(
                "div > div.uitk-grid.all-grid-fallback-alt > div.uitk-col.all-col-fill.custom-short-r-margin > div")
            flight_departure_datetime = flight_info.find_element_by_css_selector(
                "div > div > div.uitk-col.tablet-col-1-3.desktop-col-1-3.custom-col-r-margin.min-width-large-screens-only > div.primary-content.no-wrap.custom-primary-padding > span > span:nth-child(1)").text
            flight_arrival_datetime = flight_info.find_element_by_css_selector(
                "div > div > div.uitk-col.tablet-col-1-3.desktop-col-1-3.custom-col-r-margin.min-width-large-screens-only > div.primary-content.no-wrap.custom-primary-padding > span > span:nth-child(2)").text
            flight_company = flight_info.find_element_by_css_selector(
                "div > div > div.uitk-col.tablet-col-1-3.desktop-col-1-3.custom-col-r-margin.min-width-large-screens-only > div.secondary-content.overflow-ellipsis.inline-children > span").text
            flight_time = flight_info.find_element_by_css_selector(
                "div > div > div.uitk-col.tablet-col-1-2.desktop-col-1-2.all-col-fill > div.fluid-content.inline-children.custom-primary-padding > span.duration-emphasis").text

            ##여기 수정할것.
            if flight_info.find_elements_by_css_selector(
                "div > div > div.uitk-col.tablet-col-1-3.desktop-col-1-3.custom-col-r-margin.min-width-large-screens-only > div.primary-content.no-wrap.custom-primary-padding > span.primary-sub-content.urgency").count != 0:
                arrival_date = new_departure_date + timedelta(days=1)
            else :
                arrival_date = self.departure_date

            price_info = flight.find_element_by_css_selector(
                'div > div.uitk-grid.all-grid-fallback-alt > div.uitk-col.all-col-shrink')

            ##여기 수정할것.
            price_raw = price_info.find_element_by_css_selector(
                'div > div.uitk-col.custom-width.all-col-fill > div.primary-content').text
            price = int(sub(r'[\d.*?^\d.]', '', price_raw))

            url_link = driver.current_url


            #  a tag 클릭해야함
            # waypoint=flight.find_element_by_css_selector("#section-offer-leg0-details > div > div.layover-info > span.layover-city").text
            # waypoint_duration = flight.find_element_by_css_selector("#section-offer-leg0-details > div > div.layover-info > span.layover-duration").text

            # new_departure_date = datetime.strftime(datetime.strptime(departure_date, '%Y.%m.%d'), '%Y-%m-%d')
            # price = self.get_flight_price_from_webpage(flight)
            # flight.find_element_by_class_name()

            # flight.find_element_by_class_name('grid-container').find_element_by_class_name(
            #     'all-col-shrink').find_element_by_class_name('standard-col-l-margin').click()
            # driver.implicitly_wait(5)
            #
            # arrival_time = self.get_flight_time_from_webpage(flight)
            # arrival_price = self.get_flight_price_from_webpage(flight)

            # new_arrival_date = datetime.strftime(datetime.strptime(arrival_date, '%Y.%m.%d'), '%Y-%m-%d')
            # new_arrival_date   = datetime.strftime(datetime.strftime(arrival_date,'%Y.%m.%d'),'%Y-%m-%d')

            result.append({
                'origin_place': origin_place,
                'destination_place': destination_place,
                'is_direct': False,
                'way_point': 'test',
                'way_point_duration': 'testtime',
                'ticket_price': price,
                'departure_date': self.departure_date,
                'departure_datetime': flight_departure_datetime,
                'arrival_date': arrival_date,
                'arrival_datetime': flight_arrival_datetime,
                'flight_time': flight_time,
                'flight_company': flight_company,
                'currency': '환율',
                'data_source': '익스피디아',
                'url_link': url_link

            })

        return result


if __name__ == '__main__':
    from ticket.models import TicketData

    crawler = TicketDetailData()

    ticket_datas = crawler.get_ticket_information()

    for ticket_data in ticket_datas:
        # 도시, 회사정보 저장
        city, _ = TicketData.objects.get_or_create(
            origin_place=ticket_data['origin_place'],
            destination_place=ticket_data['destination_place'],
            is_direct=ticket_data['is_direct'],
            way_point=ticket_data['way_point'],
            way_point_duration=ticket_data['way_point_duration'],
            ticket_price=ticket_data['ticket_price'],

            departure_date=ticket_data['departure_date'],
            departure_datetime=ticket_data['departure_datetime'],
            arrival_date=ticket_data['arrival_date'],
            arrival_datetime=ticket_data['arrival_datetime'],

            flight_company=ticket_data['flight_company'],
            currency=ticket_data['currency'],
            data_source=ticket_data['data_source'],
            url_link=ticket_data['url_link'],
        )
