from selenium import webdriver
import csv
import time
from selenium.webdriver.support.ui import WebDriverWait
from Logging import log
import Website
import pandas as pd

# INIT


header = ['Site', 'Pet', 'Breed', 'Age', 'Gender', 'Neutered', 'Purchase Price', 'Monthly', 'Yearly', 'Vet Excess',
          'Annual Condition Limit']


df = pd.read_csv('C:/Users/jbateman/Documents/PetPlanCatchUp.csv',  encoding = "ISO-8859-1")
count_df_rows = df.shape[0]


def MainPageLoad(driver, csv_writer, dtrow):
    url = Website.site(dtrow[0])
    wait = WebDriverWait(driver, 30)
    log('Navigate to ' + dtrow[0])
    try:
        driver.get(url)
    except:
        log(("Driver Failure"))
        print('Driver Fail')
    Website.PetSite(dtrow, csv_writer, driver, wait)
    driver.delete_all_cookies()


with open("PetPlanResultsCatchUp.csv", 'wt', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(header)
    time.sleep(5)
    log('<----STARTING PROCESS---->')
    for index, dtrow in df.iterrows():
        time.sleep(1)
        driver = webdriver.Chrome("C:/Users/jbateman/AppData/Local/Programs/Python/Python37/scripts/"
                                  "chromedriver.exe")
        driver.set_page_load_timeout('10')
        MainPageLoad(driver, csv_writer, dtrow)
        time.sleep(2)
        driver.close()
        print(str(index + 1) + ' out of ' + str(count_df_rows) + ' Transaction Complete')
    log('<----PROCESS COMPLETE---->')
