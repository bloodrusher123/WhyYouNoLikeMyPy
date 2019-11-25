import csv
from selenium import webdriver
import datetime
from selenium.webdriver.common.keys import Keys
import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)
driver = webdriver.Chrome("C:/Users/jbateman/AppData/Local/Programs/Python/Python37/scripts/chromedriver.exe")
Sites = ['Go Compare', 'Compare the Market', 'Money Supermarket', 'Insurers']
dictExtract = {
    'Site': Sites[0],
    'AggQuote': '',
    'BrandQuote': '',
    'Top': '',
    'Clicks': ''
}
header = ['Site', 'AggQuote', 'BrandQuote', 'Top', 'Clicks']


def rowFunc(dictextract, site):
    row = site, dictextract['AggQuote'].text, dictextract['BrandQuote'].text, dictextract['Top'].text, dictextract[
        'Clicks'].text
    return row


with open("results.csv", 'wt') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(header)


#def GoCompareCar(dictExtract, csv_writer):
    site = Sites[0]
    driver.set_page_load_timeout("10")
    driver.get("https://snapshot.gocompare.com")
    time.sleep(1)
    driver.find_element_by_id("ctl00_PlaceHolderMain_txtUsername").send_keys("ian.davies@insurancefactory.co.uk")
    driver.find_element_by_id("ctl00_PlaceHolderMain_txtPassword").send_keys("b]ER(#Te")
    driver.find_element_by_id("ctl00_PlaceHolderMain_btnLogin").send_keys(Keys.ENTER)
    time.sleep(2)
    driver.get("https://snapshot.gocompare.com/bi/pages/performancevols-daily.aspx")
    time.sleep(5)
    driver.find_element_by_id("daterange").click()
    driver.find_element_by_xpath("/html/body/div/div[3]/ul/li[1]").click()
    # driver.find_element_by_class_name("applyBtn btn btn-small btn-sm btn-success")
    time.sleep(10)
    dictExtract['AggQuote'] = driver.find_element_by_xpath(
        "/html/body/form/div[12]/div/div/div[4]/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/div/div[1]/div/div/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr/td[4]/table/tbody/tr/td/div/div/div/table/tbody/tr[4]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]/td[2]/table/tbody/tr[4]/td[4]/div")
    dictExtract['BrandQuote'] = driver.find_element_by_xpath(
        "/html/body/form/div[12]/div/div/div[4]/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/div/div[1]/div/div/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr/td[4]/table/tbody/tr/td/div/div/div/table/tbody/tr[4]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]/td[2]/table/tbody/tr[4]/td[6]/div")
    dictExtract['Top'] = driver.find_element_by_xpath(
        "/html/body/form/div[12]/div/div/div[4]/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/div/div[1]/div/div/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr/td[4]/table/tbody/tr/td/div/div/div/table/tbody/tr[4]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]/td[2]/table/tbody/tr[4]/td[11]/div")
    dictExtract['Clicks'] = driver.find_element_by_xpath(
        "/html/body/form/div[12]/div/div/div[4]/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/div[2]/div/div/div[1]/div/div/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr/td[4]/table/tbody/tr/td/div/div/div/table/tbody/tr[4]/td[3]/div/div[1]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]/td[2]/table/tbody/tr[4]/td[16]/div")
    print(dictExtract['AggQuote'].text, dictExtract['BrandQuote'].text, dictExtract['Top'].text,
          dictExtract['Clicks'].text)
    row = rowFunc(dictExtract, site)
    csv_writer.writerow(row)

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)

    site = Sites[1]
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div/div[2]/div[42]/div/div/div/div[1]/div[11]/div[1]/div[2]/canvas[2]")
