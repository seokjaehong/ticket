import ast
import datetime
import json
from datetime import timedelta
import time
import random

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from ticket.models.ticketdata import TicketData


# class_grade(d) : 할인석
# class_grade(n) : 일반석
# class_grade(b) : 비즈니스석
# 할인/일반석 만 포함


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def parser_raw_value_to_datefield(raw_value):
    departure_date_string = raw_value[:4] + '-' + raw_value[4:6] + '-' + raw_value[6:8]
    departure_date = datetime.date(*(int(s) for s in departure_date_string.split('-')))
    return departure_date

def generator_rand_num():
    return random.randrange(1,10)

def get_ticket_information_single_date(origin_place, destination_place, departure_date, flight_company):
    """
    class_grade(d) : 할인석
    class_grade(n) : 일반석
    class_grade(b) : 비즈니스석

    :param origin_place:
    :param destination_place:
    :param departure_date:
    :return:
    """

    start_time = time.time()
    print(flight_company)
    url = "http://air" + str(generator_rand_num()) + ".jeju.com/item/ajax/ajax.air_search_v3.php" \
          "?flight_index=1" \
          "&flight_scity=" + origin_place + \
          "&flight_ecity=" + destination_place + \
          "&flight_date=" + str(departure_date) + \
          "&flight_com=" + str(flight_company) + \
          "&flight_class%5B%5D=b" \
          "&flight_class%5B%5D=n" \
          "&flight_class%5B%5D=d" \
          "&flight_adult=1" \
          "&flight_junior=0" \
          "&flight_baby=0" \
          "&agt=jeju" \
          "&time=1531298088800&_=1531298088202"
    response = requests.get(url)
    # soup = BeautifulSoup(response.text, 'lxml')
    # s = ast.literal_eval(soup.text)['data']
    r=response.text.replace("(","").replace(")","")
    s=json.loads(r)['data']
    print(s)
    print("---(url) %s seconds ---" % (time.time() - start_time))
    result = []
    for i in s:
        obj, created = TicketData.objects.update_or_create(
            origin_place=s[i]["dep_desc"],
            destination_place=s[i]['arr_desc'],
            is_direct=False,
            way_point='',
            way_point_duration='',
            ticket_price=int(s[i]['total']),
            departure_date=parser_raw_value_to_datefield(s[i]['dep_date_time']),
            departure_datetime=s[i]['dep_time'],
            arrival_date=parser_raw_value_to_datefield(s[i]['arr_date_time']),
            arrival_datetime=s[i]['arr_time'],
            flight_time=s[i]['term'],
            flight_company=s[i]['car_desc'],
            currency='KRW',
            data_source='jeju.com',
            leftseat=s[i]['no_of_avail_seat'],
        )
        result.append(obj)
        # print(obj)
    print("---(end) %s seconds ---" % (time.time() - start_time))
    return result


def get_ticket_information_single_date_selenium(origin_place, destination_place, departure_date):
    start_time = time.time()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument('no-sandbox')
    options.add_argument("disable-setuid-sandbox")
    options.add_argument('disable-dev-shm-usage')
    # options.add_argument('disable-extensions')

    # #광고 차단
    # prefs = {'profile.managed_default_content_settings.images': 2}
    # options.add_experimental_option('prefs', prefs)

    driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=options)

    url = "http://www.jeju.com/item/air_list.html?agt=jeju&flight_type=1" \
          "&flight_scity=" + "GMP" + \
          "&flight_ecity=" + "CJU" + \
          "&flight_sdate=" + "2018-08-01" + \
          "&flight_edate=" + "2018-08-01" + \
          "&boarding_adult=1&boarding_junior=0&boarding_baby=0"
    print("---(url) %s seconds ---" % (time.time() - start_time))
    driver.get(url)
    print("---(driver ok) %s seconds ---" % (time.time() - start_time))
    driver.implicitly_wait(3)
    driver.maximize_window()
    print("---(maximize) %s seconds ---" % (time.time() - start_time))

    # flight_information_list = driver.find_elements_by_xpath("//*[@id='tableDepList']/tbody/tr")
    flight_information_list = driver.find_elements_by_css_selector("#tableDepList > tbody > tr")

    print("---(tbody) %s seconds ---" % (time.time() - start_time))

    for flight_information in flight_information_list:
        if flight_information.text != "매진\n국내 7개 항공사의 모든 항공권이 매진되었습니다.\n다른 날짜를 선택해주세요.":
            flight_company = flight_information.get_attribute("car_desc")
            departure_datetime = flight_information.get_attribute("dep_time_str")
            arrival_datetime = flight_information.get_attribute("arr_time_str")
            leftseat = flight_information.get_attribute("no_of_avail_seat")
            ticket_price = int(flight_information.get_attribute("price"))
            flight_time = flight_information.get_attribute("term")

            obj, created = TicketData.objects.get_or_create(
                origin_place=origin_place,
                destination_place=destination_place,
                is_direct=False,
                way_point='',
                way_point_duration='',
                ticket_price=ticket_price,
                departure_date=departure_date,
                departure_datetime=departure_datetime,
                arrival_date=departure_date,
                arrival_datetime=arrival_datetime,
                flight_time=flight_time,
                flight_company=flight_company,
                currency='KRW',
                data_source='jeju.com',
                leftseat=leftseat,
            )

            print("---(total day)crawler %s seconds ---" % (time.time() - start_time))
            driver.close()
            return obj
        else:
            print("---(total day)crawler %s seconds ---" % (time.time() - start_time))
            return '매진'
