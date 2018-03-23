from re import sub

import requests
from bs4 import BeautifulSoup
from decimal import Decimal
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_url(startdate, enddate, startcity, endcity):
    url = "https://www.expedia.co.kr/Flights-Search?flight-type=on&starDate=" + startdate + \
          "&endDate=" + enddate + "" \
                                  "&_xpid=11905%7C1" \
                                  "&mode=search" \
                                  "&trip=roundtrip" \
                                  "&leg1=from%3A%EC%84%9C%EC%9A%B8%2C+%ED%95%9C%EA%B5%AD+%28" \
          + startcity + "-%EB%AA%A8%EB%93%A0+%EA%B3%B5%ED%95%AD%29%2Cto%3A%EB%B6%80%EC%82%B0%2C+%ED%95%9C%EA%B5%AD+%28" \
          + endcity + "-%EA%B9%80%ED%95%B4%EA%B5%AD%EC%A0%9C%EA%B3%B5%ED%95%AD%29%2Cdeparture%3A2018.03.31TANYT&leg2=from%3A%EB%B6%80%EC%82%B0%2C+%ED%95%9C%EA%B5%AD+%28PUS-%EA%B9%80%ED%95%B4%EA%B5%AD%EC%A0%9C%EA%B3%B5%ED%95%AD%29%2Cto%3A%EC%84%9C%EC%9A%B8%2C+%ED%95%9C%EA%B5%AD+%28SEL-%EB%AA%A8%EB%93%A0+%EA%B3%B5%ED%95%AD%29%2Cdeparture%3A2018.04.24TANYT&passengers=children%3A0%2Cadults%3A1%2Cseniors%3A0%2Cinfantinlap%3AY"

    return url


def get_ticket_information():
    result = list()

    def get_time_price_from_home_page():
        time_info = flight_infomation.find_element_by_class_name('flight-module').find_element_by_class_name(
            'primary-content').text
        price_raw = flight_infomation.find_element_by_class_name('grid-container').find_element_by_class_name(
            'all-col-shrink').find_element_by_class_name('primary-content')

        price_info = int(sub(r'[^\d.]', '', price_raw.text))
        result.append({'time': time_info, 'price': price_info})
        return result

    flight_infomation = driver.find_element_by_id('flight-listing-container')

    departure_info = get_time_price_from_home_page()

    flight_infomation.find_element_by_class_name('grid-container').find_element_by_class_name(
        'all-col-shrink').find_element_by_class_name('standard-col-l-margin').click()
    driver.implicitly_wait(5)

    arrival_info = get_time_price_from_home_page()

    return result


driver = webdriver.Chrome('chromedriver')
driver.implicitly_wait(3)

url = get_url('2018.03.31', '2018.04.24', 'SEL', 'PUS')
driver.get(url)

result = get_ticket_information()
print(result)
