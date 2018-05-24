import os
import sys
import time
from datetime import datetime
from datetime import timedelta
from re import sub

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django

django.setup()


class TwayData():
    def get_ticket_information(self):
        driver = webdriver.Chrome('chromedriver')
        url = "https://www.twayair.com/main.do#;"
        driver.get(url)
        action = action_chains.ActionChains(driver)
        driver.implicitly_wait(3)

        flight_informations = driver.find_element_by_xpath(
            "//*[@id='header']/div[3]/div[2]/ul/li[1]/form/fieldset/div/div/ul")
        #편도선택
        flight_informations.find_element_by_xpath("//*[@id='header']/div[3]/div[2]/ul/li[1]/form/fieldset/div/ul/li[2]/label").click()
        #노선선택
        flight_informations.find_element_by_xpath("li[1]/a").click()
        #김포제주
        flight_informations.find_element_by_xpath("li[1]/section/div/dl[1]/dd[1]/a").click()

        # 가는날자, 사람수 선택, 확인버튼 클릭
        driver.find_element_by_xpath("//*[@id='onwardDatepicker']/div/div[2]/div/table/tbody/tr[4]/td[6]/a").click()

        # driver.find_element_by_xpath("//*[@id='returnDatepicker']/div/div[2]/div/table/tbody/tr[5]/td[4]/a").click()
        driver.find_element_by_xpath(
            "//*[@id='header']/div[3]/div[2]/ul/li[1]/form/fieldset/div/div/ul/li[2]/section/div/div[3]/div[1]/button").click()
        driver.implicitly_wait(1)
        #//*[@id="header"]/div[3]/div[2]/ul/li[1]/form/fieldset/div/div/ul/li[2]/section/div/div[3]/div[1]/button
        driver.find_element_by_xpath(
            "//*[@id='header']/div[3]/div[2]/ul/li[1]/form/fieldset/div/div/ul/li[4]/section/div/p[3]/a").click()
        driver.maximize_window()

        # 화면 넘어갈 때 필요한 클릭질,
        webElement = driver.find_element_by_css_selector("#ancBooking")
        webElement.click()

        driver.implicitly_wait(2)
        driver.find_element_by_xpath("//*[@id='btnConfirmRouteNotice']").click()
        driver.implicitly_wait(2)

        departure_date=driver.find_element_by_xpath("//*[@id='divSelectByDate']/div/div/ul[2]/li[1]/a").text
        new_departure_date=datetime.strptime(departure_date, "%Y/%m/%d")

        # departure_date = driver.find_element_by_xpath("//*[@id='resultbox1']/div[2]/ul/li[4]/a/span").text
        # arrival_date = driver.find_element_by_xpath("//*[@id='resultbox2']/div[2]/ul/li[4]/a/span").text

        ticket_informations = driver.find_elements_by_xpath("//*[@id='tbodyOnward']/tr")

        result = []
        for ticket in ticket_informations:
            if ticket.get_attribute("class") != "trOnward":
                departure_datetime = ticket.find_element_by_xpath("td[1]/div").text
                print(departure_datetime)
                arrival_datetime = ticket.find_element_by_xpath("td[3]").text
                flight_time = ticket.find_element_by_xpath("td[4]/span[2]").text
                print(arrival_datetime)
                price = int(sub(',','',ticket.find_element_by_xpath("td[6]/label/span").text))
                # pricesub(',','',price)
                print(price)

            result.append({
                'origin_place': 'GMP',
                'destination_place': 'CJU',
                'is_direct': True,
                'way_point': 'None',
                'way_point_duration': 'None',
                'ticket_price': price,
                'departure_date': new_departure_date,
                'departure_datetime': departure_datetime,
                'arrival_date': new_departure_date,
                'arrival_datetime': arrival_datetime,
                'flight_time': flight_time,
                'flight_company': 'tway',
                'currency': '환율',
                'data_source': 'tway',
                # 'url_link':

            })
        return result


if __name__ == '__main__':
    from ticket.models import TicketData
    crawler = TwayData()
    ticket_datas = crawler.get_ticket_information()

    for ticket_data in ticket_datas:
        print(ticket_data)
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
            # url_link='',
        )
