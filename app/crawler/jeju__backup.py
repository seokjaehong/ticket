# 코드 재작성. crawler>management>commands> job_jeju.py
# from datetime import timedelta
#
# from selenium import webdriver
# import time
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
# from crawler.utils import daterange
#
# from selenium.common.exceptions import  NoSuchElementException
# from selenium.common.exceptions import TimeoutException
#
# __all__ = (
#     'JejuData',
# )
#
#
# class JejuData():
#     def __init__(self):
#         self.origin_place = None
#         self.destination_place = None
#         self.is_direct = False
#         self.way_point = None
#         self.way_point_duration = None
#         self.ticket_price = 0
#         self.departure_date = ''
#         self.departure_datetime = ''
#         self.arrival_date = ''
#         self.arrival_datetime = ''
#         self.flight_time = ''
#         self.leftseat = ''
#         self.flight_company = None
#         self.currency = 'KRW'
#         self.data_source = 'jeju.com'
#         self.description = ''
#
#     def get_ticket_detail(self, driver, departure_date, origin_place, destination_place):
#         result = list()
#         flight_information_list = driver.find_elements_by_xpath("//*[@id='tableDepList']/tbody/tr")
#         for flight_information in flight_information_list:
#             # print(flight_information.text)
#             if flight_information.text != "매진\n국내 7개 항공사의 모든 항공권이 매진되었습니다.\n다른 날짜를 선택해주세요.":
#                 flight_company = flight_information.get_attribute("car_desc")
#                 departure_datetime = flight_information.get_attribute("dep_time_str")
#                 arrival_datetime = flight_information.get_attribute("arr_time_str")
#                 leftseat = flight_information.get_attribute("no_of_avail_seat")
#                 ticket_price = int(flight_information.get_attribute("price"))
#                 flight_time = flight_information.get_attribute("term")
#
#                 result.append({
#                     'origin_place': origin_place,
#                     'destination_place': destination_place,
#                     'is_direct': False,
#                     'way_point': 'None',
#                     'way_point_duration': 'None',
#                     'ticket_price': ticket_price,
#                     'departure_date': departure_date,
#                     'departure_datetime': departure_datetime,
#                     'arrival_date': departure_date,
#                     'arrival_datetime': arrival_datetime,
#                     'flight_time': flight_time,
#                     'flight_company': flight_company,
#                     'currency': 'KRW',
#                     'data_source': 'jeju.com',
#                     'leftseat': leftseat,
#                 })
#         return result
#
#     def get_ticket_information(self, origin_place=None, destination_place=None, departure_date=None, add_days=None):
#
#         start_time = time.time()
#         options = webdriver.ChromeOptions()
#         options.add_argument('headless')
#         options.add_argument('window-size=1920x1080')
#         options.add_argument("disable-gpu")
#         options.add_argument('no-sandbox')
#         options.add_argument("disable-setuid-sandbox")
#         options.add_argument('disable-dev-shm-usage')
#         driver = webdriver.Chrome('/usr/local/bin/chromedriver')
#
#         def not_busy(driver):
#             try:
#                 element = driver.find_elements_by_xpath("//*[@id='tableDepList']/tbody/tr")
#             except NoSuchElementException:
#                 return False
#             return element.get_attribute("//*[@id='div_searching_1']") == "false"
#
#         url = "http://www.jeju.com/item/air_list.html?agt=jeju&flight_type=1" \
#               "&flight_scity=" + origin_place + \
#               "&flight_ecity=" + destination_place + \
#               "&flight_sdate=" + str(departure_date) + \
#               "&flight_edate=" + str(departure_date) + \
#               "&boarding_adult=1&boarding_junior=0&boarding_baby=0"
#
#         driver.get(url)
#         driver.implicitly_wait(3)
#         driver.maximize_window()
#
#         end_date = departure_date + timedelta(days=add_days)
#         print('end_date:', end_date)
#         result = list()
#
#         wait = WebDriverWait(driver, 5, poll_frequency=0.1)
#         for single_date in daterange(departure_date, end_date=end_date):
#             # print('single_date:', single_date)
#
#             try:
#                 single_result = self.get_ticket_detail(driver, single_date, origin_place, destination_place)
#
#                 result.append(single_result)
#                 next_box = driver.find_element_by_xpath("//*[@id='airline1_next']")
#                 next_box.click()
#
#                 wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#div_searching_1[style=none]")))
#                 # wait.until(wait_for_the_attribute_value((By.CSS_SELECTOR, "#div_searching_1"), "style", "none"))
#
#                 print("Page is ready!")
#
#             except TimeoutException:
#                 print("Loading took too much time!")
#
#             # print("---(single day)crawler %s seconds ---" % (time.time() - start_time))
#
#         print("---(total day)crawler %s seconds ---" % (time.time() - start_time))
#
#         driver.close()
#         return result
