import os
from datetime import datetime
from re import sub

from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.common.exceptions import NoSuchElementException
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
# import django

# django.setup()

__all__ = (
    'TwayData',
)


class TwayData():
    def __init__(self):
        self.origin_place = 'GMP'
        self.destination_place = 'CJU'
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

    def get_ticket_information(self, year, month, date):
        driver = webdriver.Chrome('chromedriver')
        url = "https://www.twayair.com/main.do#;"
        driver.get(url)
        driver.implicitly_wait(3)

        def yearpicker(year):
            elements = driver.find_elements_by_xpath(
                "//*[@id='onwardDatepicker']/div/div[2]/div/div/select[2]/option")

            for years in elements:
                if years.text == year:
                    years.click()
                    break

        def monthpicker(month):
            elements = driver.find_elements_by_xpath(
                "//*[@id='onwardDatepicker']/div/div[2]/div/div/select[1]/option")

            for months in elements:
                if months.text == month:
                    months.click()
                    break

        def datepicker(date):
            elements = driver.find_elements_by_xpath(
                "//*[@id='onwardDatepicker']/div/div[2]/div/table/tbody/tr/td/a")

            for dates in elements:
                if dates.is_enabled() and dates.is_displayed() and str(dates.get_attribute("title")) == date:
                    dates.click()
                    break

        flight_informations = driver.find_element_by_xpath(
            "//*[@id='header']/div[3]/div[2]/ul/li[1]/form/fieldset/div/div/ul")

        # 편도선택
        flight_informations.find_element_by_xpath(
            "//*[@id='header']/div[3]/div[2]/ul/li[1]/form/fieldset/div/ul/li[2]/label").click()
        # 노선선택
        flight_informations.find_element_by_xpath("li[1]/a").click()
        # 김포제주
        flight_informations.find_element_by_xpath("li[1]/section/div/dl[1]/dd[1]/a").click()

        # 가는날짜, 사람수 선택, 확인버튼 클릭
        yearpicker(year)
        monthpicker(month)
        datepicker(date)
        # self.driver.find_element_by_xpath(
        #     "//*[@id='onwardDatepicker']/div/div[2]/div/table/tbody/tr[4]/td[6]/a").click()

        driver.find_element_by_xpath(
            "//*[@id='header']/div[3]/div[2]/ul/li[1]/form/fieldset/div/div/ul/li[2]/section/div/div[3]/div[1]/button").click()
        driver.implicitly_wait(1)
        driver.find_element_by_xpath(
            "//*[@id='header']/div[3]/div[2]/ul/li[1]/form/fieldset/div/div/ul/li[4]/section/div/p[3]/a").click()
        driver.maximize_window()

        # 화면 넘어갈 때 필요한 확인버튼 클릭
        webElement = driver.find_element_by_css_selector("#ancBooking")
        webElement.click()

        driver.implicitly_wait(2)
        driver.find_element_by_xpath("//*[@id='btnConfirmRouteNotice']").click()
        driver.implicitly_wait(2)

        departure_date = driver.find_element_by_xpath("//*[@id='divSelectByDate']/div/div/ul[2]/li[1]/a").text
        new_departure_date = datetime.strptime(departure_date, "%Y/%m/%d")

        ticket_informations = driver.find_elements_by_xpath("//*[@id='tbodyOnward']/tr")

        result = []
        for ticket in ticket_informations:
            if ticket.get_attribute("class") != "trOnward":

                departure_datetime = ticket.find_element_by_xpath("td[1]/div").text
                arrival_datetime = ticket.find_element_by_xpath("td[3]").text
                flight_time = ticket.find_element_by_xpath("td[4]/span[2]").text
                price = int(sub(',', '', ticket.find_element_by_xpath("td[6]/label/span").text))

                try:
                    leftseat = ticket.find_element_by_xpath("td[6]/p/em").text
                except NoSuchElementException:
                    leftseat = ""

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
        driver.close()
        return result



# if __name__ == '__main__':
#     # from ticket.models import TicketData
#
#     from ticket.models.ticketdata import TicketData
#
#     crawler = TwayData()
#     ticket_datas = crawler.get_ticket_information('2018', '07', '11')
#
#     for ticket_data in ticket_datas:
#         # print(ticket_data)
#         # 도시, 회사정보 저장
#         city, _ = TicketData.objects.update_or_create(
#             origin_place=ticket_data['origin_place'],
#             destination_place=ticket_data['destination_place'],
#             is_direct=ticket_data['is_direct'],
#             way_point=ticket_data['way_point'],
#             way_point_duration=ticket_data['way_point_duration'],
#             ticket_price=ticket_data['ticket_price'],
#
#             departure_date=ticket_data['departure_date'],
#             departure_datetime=ticket_data['departure_datetime'],
#             arrival_date=ticket_data['arrival_date'],
#             arrival_datetime=ticket_data['arrival_datetime'],
#             flight_time=ticket_data['flight_time'],
#             flight_company=ticket_data['flight_company'],
#             currency=ticket_data['currency'],
#             data_source=ticket_data['data_source'],
#             leftseat=ticket_data['leftseat'],
#             # url_link='',
#         )
