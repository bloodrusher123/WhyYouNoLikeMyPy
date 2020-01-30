from selenium import webdriver
import page
from selenium.webdriver.support.ui import Select
import csv
import time
from selenium.webdriver.support.ui import WebDriverWait
from Logging import log

def site(site):
    if 'Tesco' in site:
        url = 'https://pet.tescobank.com/quoteAndBuy.do'
    elif 'Pet Plan' in site:
        url = 'https://quote.petplan.co.uk/step-1'
    else:
        url = 'https://www.animalfriendsquote.co.uk'
    return url

def PetSite(dtrow, csv_writer, driver, wait):
    try:
        if 'Tesco' in dtrow[0]:
            log('Entering Details...')
            page.TescoPetPage(driver, wait, dtrow)
            log('Generating Quote')
            page.TescoYourQuote(driver, wait, csv_writer, dtrow)
            log(dtrow[0] + ' ' + dtrow[2] + ' Complete')

        elif 'Animal Friends' in dtrow[0]:
            if 'Cat' in dtrow[1]:
                log('Cat')
                page.AnimalFriendsCat(driver, wait, dtrow)
                log('Generating Quote')
                page.AnimalFriendsQuotePage(driver, wait, csv_writer, dtrow)
                log(dtrow[0] + ' ' + dtrow[2] + ' Complete')
            elif 'Crossbreed' in dtrow[2]:
                log('Mixed Breed')
                page.AnimalFriendsMix(driver, wait, dtrow)
                log('Generating Quote')
                page.AnimalFriendsQuotePage(driver, wait, csv_writer, dtrow)
                log(dtrow[0]+ ' ' + dtrow[2] + ' Complete')

            elif 'Dog' in dtrow[1]:
                log('Pedigree Dog')
                page.AnimalFriendsDog(driver, wait, dtrow)
                log('Generating Quote')
                page.AnimalFriendsQuotePage(driver, wait, csv_writer, dtrow)
                log(dtrow[0] + ' ' + dtrow[2] + ' Complete')
        elif 'Pet Plan' in dtrow[0]:
            log('Entering Details on Pet Plan')
            page.PetPlanPetDetails(driver, wait, dtrow)
            log('Entering Owner Details')
            page.PetPlan_OwnerDetailsPage(driver, wait)
            log('Pet Plan Quote Page Present')
            page.PetPlan_QuotePage(driver, wait, csv_writer, dtrow)


    except:
        row = dtrow[0], dtrow[1], dtrow[2], dtrow[3], dtrow[4], dtrow[5], "Failed to Extract", "", "",""
        csv_writer.writerow(row)
        log('There Was an Error')