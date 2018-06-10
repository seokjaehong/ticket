import re
from decimal import Decimal
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


def makeURL(start, arrive, start_date, arrive_date):
    pass


def checkcity(start, arrive):
    city = dict()
    city['서울'] = 'ICN,GMP'
    city['로마'] = 'FCO,CIA,IRT,XRJ'
    city['피렌체'] = 'FLR,FIR,ZMS'
    city['프라하'] = 'PRG,XYG'
    return city[start], city[arrive]


def searchFlight(url, start=False):
    driver = webdriver.Chrome('chromedriver')
    driver.implicitly_wait(6)
    driver.get(url)

    price_string = driver.find_element_by_class_name('LJV2HGB-d-Bb').text
    time = driver.find_element_by_class_name("LJV2HGB-d-ac").text
    flight_time = driver.find_element_by_class_name("LJV2HGB-d-Jb").text
    transfer = driver.find_element_by_class_name("LJV2HGB-d-Sb").text

    driver.implicitly_wait(10)
    choice = list()
    price = Decimal(re.sub(r'[^\d.]', '', price_string)) * 1000
    choice.append(price)
    choice.append(time)
    choice.append(flight_time)
    choice.append(transfer)

    if start:
        driver.find_element_by_class_name('LJV2HGB-d-Bb').click()
        driver.implicitly_wait(20)
        ch_url = driver.current_url
        driver.implicitly_wait(20)
        # searchFlight(ch_url)
        return ch_url, choice

    else:
        return choice


start, arrive = checkcity('서울', '피렌체')

# start, arrive = checkcity('서울', '프라하')
url = "https://www.google.com/flights/#search;" + "f=" + start + ";t=" + arrive + ";d=2018-04-08;r=2018-04-12"

url, result = searchFlight(url, start=True)
for item in result:
    print(item)
print('하나끝남!')
a = searchFlight(url, start=False)
for item in a:
    print(item)
