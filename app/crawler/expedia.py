from re import sub

from selenium import webdriver

driver = webdriver.Chrome('chromedriver')

departure_date = '2018.05.17'
arrival_date = '2018.05.19'
departure_city = 'SEL'
arrival_city = "PUS"

driver.implicitly_wait(3)
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
def get_flight_time_from_webpage(obj):
    time_info = obj.find_element_by_class_name('flight-module').find_element_by_class_name(
            'primary-content')
    return time_info

def get_flight_price_from_webpage(obj):
    price_raw = obj.find_element_by_class_name('grid-container').find_element_by_class_name(
        'all-col-shrink').find_element_by_class_name('primary-content')

    price_info = int(sub(r'[^\d.]', '', price_raw.text))
    return price_info

def get_ticket_information():
    flight_infomations = driver.find_element_by_id('flight-listing-container')

    for flight in flight_infomations :
        departure_time = get_flight_time_from_webpage(flight)
        departure_price = get_flight_price_from_webpage(flight)

        flight.find_element_by_class_name('grid-container').find_element_by_class_name(
            'all-col-shrink').find_element_by_class_name('standard-col-l-margin').click()
        driver.implicitly_wait(5)

        arrival_time = get_flight_time_from_webpage(flight_infomation)
        arrival_price = get_flight_price_from_webpage(flight_infomation)



result = get_ticket_information()
print(result)
