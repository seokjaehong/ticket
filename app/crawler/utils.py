from datetime import timedelta
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from ticket.models.ticketdata import TicketData


def get_clear_browsing_button(driver):
    """Find the "CLEAR BROWSING BUTTON" on the Chrome settings page."""
    return driver.find_element_by_css_selector('* /deep/ #clearBrowsingDataConfirm')


def clear_cache(driver, timeout=60):
    """Clear the cookies and cache for the ChromeDriver instance."""
    # navigate to the settings page
    driver.get('chrome://settings/clearBrowserData')

    # wait for the button to appear
    wait = WebDriverWait(driver, timeout)
    wait.until(get_clear_browsing_button)

    # click the button to clear the cache
    get_clear_browsing_button(driver).click()

    # wait for the button to be gone before returning
    wait.until_not(get_clear_browsing_button)


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def get_ticket_information_single_date(origin_place, destination_place, departure_date):
    print(departure_date)
    print(type(departure_date))
    start_time = time.time()
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument('no-sandbox')
    options.add_argument("disable-setuid-sandbox")
    options.add_argument('disable-dev-shm-usage')
    driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=options)

    url = "http://www.jeju.com/item/air_list.html?agt=jeju&flight_type=1" \
          "&flight_scity=" + origin_place + \
          "&flight_ecity=" + destination_place + \
          "&flight_sdate=" + str(departure_date) + \
          "&flight_edate=" + str(departure_date) + \
          "&boarding_adult=1&boarding_junior=0&boarding_baby=0"

    driver.get(url)
    driver.implicitly_wait(3)
    driver.maximize_window()

    flight_information_list = driver.find_elements_by_xpath("//*[@id='tableDepList']/tbody/tr")

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
