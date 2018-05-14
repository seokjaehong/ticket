
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')
url = "http://air.ybtour.co.kr/air/b2c/AIR/MBL/AIRMBLSCH0100100010.k1?initform=RT&domintgubun=I" \
      "&depctycd=SEL" \
      "&depctycd=NRT" \
      "&depctycd=&depctycd=" \
      "&arrctycd=NRT" \
      "&arrctycd=SEL" \
      "&arrctycd=&arrctycd=&depctynm=%EC%9D%B8%EC%B2%9C%2F%EA%B9%80%ED%8F%AC&depctynm=%EB%8F%84%EC%BF%84%2F%EB%82%98%EB%A6%AC%ED%83%80&depctynm=&depctynm=&arrctynm=%EB%8F%84%EC%BF%84%2F%EB%82%98%EB%A6%AC%ED%83%80&arrctynm=%EC%9D%B8%EC%B2%9C%2F%EA%B9%80%ED%8F%AC&arrctynm=&arrctynm=" \
      "&depdt=2018-05-18" \
      "&depdt=2018-05-25" \
      "&depdt=&depdt=" \
      "&adtcount=1" \
      "&chdcount=0" \
      "&infcount=0&cabinclass=Y&preferaircd=&availcount=250&opencase=N&opencase=N&opencase=N&openday=&openday=&openday=&depdomintgbn=D&tasktype=B2C" \
      "&secrchType=FARE&maxprice=&servicecacheyn=Y&skplt=N&areacd=&KSESID=air%3Ab2c%3ASELK138AN%3AAA024%3A%3A00"
driver.get(url)
driver.implicitly_wait(5)
table_list = driver.find_element_by_xpath("//*[@id='div_fare']/tbody")
company = table_list.find_element_by_xpath("tr[1]/td[1]/ul/li[2]/strong").text
price = table_list.find_element_by_xpath("tr[1]/td[2]/span[1]").text
print(company)
print(price)
