import os
from datetime import datetime
from re import sub

from selenium import webdriver
from selenium.webdriver.common import action_chains

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django

django.setup()


class JejuData():
    def get_ticket_information(self):
        driver = webdriver.Chrome('chromedriver')
        url = "https://www.jejuair.net/jejuair/kr/com/jeju/ibe/goAvail.do"
        driver.get(url)
        driver.implicitly_wait(3)

        # 편도선택
        driver.find_element_by_xpath("//*[@id='btnSingle']").click()

        # 출발지 선택
        driver.find_element_by_xpath("//*[@id='btnDepStn1']").click()
        # 김포 선택
        driver.find_element_by_xpath("//*[@id='dl1']/dd[5]/button").click()
        # 도착지 선택
        driver.find_element_by_xpath("//*[@id='btnArrStn1']").click()
        # 제주 선택
        driver.find_element_by_xpath("//*[@id='dl1']/dd[3]/button").click()

        # 날짜 선택
        driver.find_element_by_xpath("//*[@id='dateCal1']").click()
        # 5.31
        driver.find_element_by_xpath("//*[@id='doubleCal1']/div/table/tbody/tr[5]/td[5]/a").click()
        driver.find_element_by_xpath("//*[@id='btnDoubleOk']").click()

        driver.find_element_by_xpath("//*[@id='btnSearchAirline']").click()

        driver.implicitly_wait(3)

        # departure_date=driver.find_element_by_xpath("//*[@id='txtDate1']").text
        departure_date = '2018-'+ driver.find_element_by_xpath("//*[@id='liDep2']/button/span").text
        new_departure_date = datetime.strptime(departure_date[:10], "%Y-%m-%d")
        ticket_informations = driver.find_elements_by_xpath("//*[@id='tbodyDep']/tr")
        result =[]

        for ticket_information in ticket_informations:
            departure_datetime = ticket_information.find_element_by_xpath("td[2]").text
            arrival_datetime = ticket_information.find_element_by_xpath("td[3]").text

            format = '%H:%M'
            flight_time = datetime.strptime(arrival_datetime,format)- datetime.strptime(departure_datetime,format)

            if ticket_information.find_element_by_xpath("td[5]").get_attribute("class") != "nbr":
                price = int(sub('\D', '', ticket_information.find_element_by_xpath("td[5]/div[1]/label/strong").text))

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
                'flight_company': 'Jeju',
                'currency': '환율',
                'data_source': 'JejuAir',
            })
        return result


if __name__ == '__main__':
    from ticket.models import TicketData

    crawler = JejuData()
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
            flight_time = ticket_data['flight_time'],
            flight_company=ticket_data['flight_company'],
            currency=ticket_data['currency'],
            data_source=ticket_data['data_source'],
            # url_link='',
        )
