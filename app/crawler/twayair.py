import os
import time
from datetime import datetime, timedelta
from re import sub

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

__all__ = (
    'TwayData',
)


class TwayData():
    start_time = time.time()
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome('chromedriver', chrome_options=options)

    url = "https://www.twayair.com/main.do#;"
    driver.get(url)
    driver.implicitly_wait(3)

    def __init__(self):
        self.origin_place = None
        self.destination_place = None
        self.is_direct = False
        self.way_point = None
        self.way_point_duration = None
        self.ticket_price = 0
        self.departure_date = ''
        self.departure_datetime = ''
        self.arrival_date = ''
        self.arrival_datetime = ''
        self.flight_time = ''
        self.leftseat = ''
        self.flight_company = 'tway'
        self.currency = 'KRW'
        self.data_source = 'tway'
        self.description = ''

    def yearpicker(self, year):
        elements = self.driver.find_elements_by_xpath(
            "//*[@id='onwardDatepicker']/div/div[2]/div/div/select[2]/option")
        for years in elements:
            if years.text == year:
                years.click()
                break

    def monthpicker(self, month):
        elements = self.driver.find_elements_by_xpath(
            "//*[@id='onwardDatepicker']/div/div[2]/div/div/select[1]/option")
        for months in elements:
            if months.text == month:
                months.click()
                break

    def datepicker(self, date):
        if date.startswith('0'):
            date = date[1]
        elements = self.driver.find_elements_by_xpath(
            "//*[@id='onwardDatepicker']/div/div[2]/div/table/tbody/tr/td/a")
        for dates in elements:
            if dates.is_enabled() and dates.is_displayed() and str(dates.get_attribute("title")) == date:
                dates.click()
                break

    def daterange(self, start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)

    def get_ticket_detail(self, single_date):
        self.driver.implicitly_wait(3)

        departure_date = self.driver.find_element_by_xpath("//*[@id='divSelectByDate']/div/div/ul[2]/li[1]/a").text
        new_departure_date = datetime.strptime(departure_date, "%Y/%m/%d")

        global ticket_informations
        ticket_informations = self.driver.find_elements_by_xpath("//*[@id='tbodyOnward']/tr")

        result = []
        for ticket in ticket_informations:
            if ticket.get_attribute("class") != "trOnward":
                departure_datetime = ticket.find_element_by_xpath("td[1]/div").text
                print(departure_datetime)
                arrival_datetime = ticket.find_element_by_xpath("td[3]").text
                flight_time = ticket.find_element_by_xpath("td[4]/span[2]").text
                price = int(sub(',', '', ticket.find_element_by_xpath("td[6]/label/span").text))
                leftseat = ""

                if ticket.find_elements_by_xpath("td[6]/p/em"):
                    leftseat = ticket.find_element_by_xpath("td[6]/p/em").text

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
                'currency': 'KRW',
                'data_source': 'tway',
                'leftseat': leftseat,

            })
        return result

    def get_ticket_information(self, departure_date, add_days):
        str_departure_date = str(departure_date)
        year = str_departure_date.split('-')[0]
        month = str_departure_date.split('-')[1]
        date = str_departure_date.split('-')[2]

        end_date = departure_date + timedelta(days=add_days)
        print(end_date)

        flight_informations = self.driver.find_element_by_xpath(
            "//*[@id='header']/div[3]/div[2]/ul/li[1]/form/fieldset/div/div/ul")

        # 편도선택
        flight_informations.find_element_by_xpath(
            "//*[@id='header']/div[3]/div[2]/ul/li[1]/form/fieldset/div/ul/li[2]/label").click()
        # 노선선택
        flight_informations.find_element_by_xpath("li[1]/a").click()
        # 김포제주
        flight_informations.find_element_by_xpath("li[1]/section/div/dl[1]/dd[1]/a").click()

        # 가는날짜, 사람수 선택, 확인버튼 클릭
        self.yearpicker(year)
        self.monthpicker(month)
        self.datepicker(date)

        self.driver.find_element_by_xpath(
            "//*[@id='header']/div[3]/div[2]/ul/li[1]/form/fieldset/div/div/ul/li[2]/section/div/div[3]/div[1]/button").click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath(
            "//*[@id='header']/div[3]/div[2]/ul/li[1]/form/fieldset/div/div/ul/li[4]/section/div/p[3]/a").click()
        self.driver.maximize_window()

        # 화면 넘어갈 때 필요한 확인버튼 클릭
        webElement = self.driver.find_element_by_css_selector("#ancBooking")
        webElement.click()

        self.driver.implicitly_wait(2)
        self.driver.find_element_by_xpath("//*[@id='btnConfirmRouteNotice']").click()
        self.driver.implicitly_wait(2)
        result = []
        wait = WebDriverWait(self.driver, 5)

        for single_date in self.daterange(departure_date, end_date):
            print('single_date:', single_date)
            single_result = self.get_ticket_detail(single_date)
            result.append(single_result)
            global next_day_box
            next_day_box = self.driver.find_element_by_xpath("//*[@id='resultbox1']/div[2]/ul/li[5]/a")
            next_day_box.click()
            wait.until(EC.staleness_of(next_day_box))
            print("---(single day)crawler %s seconds ---" % (time.time() - self.start_time))

        print("---(total day)crawler %s seconds ---" % (time.time() - self.start_time))
        self.driver.close()
        return result
