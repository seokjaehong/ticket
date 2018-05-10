from selenium.webdriver.chrome import webdriver


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
