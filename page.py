from locators import DetailsPageLocators, AboutYouLocators, QuotePageLocators, AnimalFriendsAnimalType, AF_Details, \
    AF_PreExistingCons, AF_QuoteType, PetPlan_PetDetails, PetPlan_OwnerDetails, PetPlan_Quote
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from Logging import log
import pyperclip
import time
import datetime

def BirthdayFromAge(Age):
    Bday = datetime.datetime.now() - datetime.timedelta(days=(Age*365)+150)
    return Bday


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

def AnimalFriendsMix(driver, wait, dtrow):
    try:
        wait.until(
            ec.visibility_of_element_located((By.XPATH, '//*[@id="details-section"]/div[1]/div[2]/div/label[2]')))
        driver.find_element(*AnimalFriendsAnimalType.Pet_Dog).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="details-section"]/div[2]/div/div[2]/div[1]/div/label[1]')))
        try:
            driver.find_element(*AF_PreExistingCons.PreConNo).click()
        except:
            log('PreCon Button Not Found')
        try:
            wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="pet-details"]/div[1]/div[1]/div/label')))
        except:
            driver.find_element(*AF_PreExistingCons.PreConNo).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="pet-details"]/div[1]/div[1]/div/label')))
        driver.find_element(*AF_Details.Pet_Name).send_keys('Thomas')
        if 'Male' in dtrow[4]:
          driver.find_element(*AF_Details.Pet_Gender_Male).click()
        elif 'Female' in dtrow[4]:
           driver.find_element(*AF_Details.Pet_Gender_Female).click()
        petDob = BirthdayFromAge(dtrow[3])
        driver.find_element(*AF_Details.Pet_DoB).send_keys(petDob.strftime('%d%m%Y'))
        driver.find_element(*AF_Details.Pet_Breed_Mixed).click()
        if 'Small' in dtrow[4]:
            driver.find_element(*AF_Details.Pet_Breed_Small).click()
        elif 'Medium' in dtrow[4]:
            driver.find_element(*AF_Details.Pet_Breed_Medium).click()
        else:
            driver.find_element(*AF_Details.Pet_Breed_Large).click()
        if 'Free' in dtrow[6]:
            driver.find_element(*AF_Details.Mix_Free).click()
        else:
            driver.find_element(*AF_Details.Mix_Paid_Btn).click()
            driver.find_element(*AF_Details.Mix_Paid_txt).send_keys(dtrow[6])
        driver.find_element(*AF_Details.Mix_NeverInsured).click()
        driver.find_element(*AF_Details.Mix_AccidentNo).click()
        driver.find_element(*AF_Details.Mix_NotDeclinedInsurance).click()
        driver.find_element(*AF_Details.Owner_FirstName).send_keys('Testing')
        driver.find_element(*AF_Details.Owner_LastName).send_keys('Testing')
        driver.find_element(*AF_Details.Owner_Email).send_keys('Test@test.com')
        driver.find_element(*AF_Details.Owner_Phone).send_keys('07814973804')
        driver.find_element(*AF_Details.Owner_DoB).send_keys('15121991')
        wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="client-details"]/div[5]/div[3]/span[2]')))
        driver.find_element(*AF_Details.Owner_ManualAddressBtn).click()
        driver.find_element(*AF_Details.Owner_Address_1).send_keys('unit 4')
        driver.find_element(*AF_Details.Owner_Address_2).send_keys('Chapman Way')
        driver.find_element(*AF_Details.Owner_Town).send_keys('Tunbridge Wells')
        driver.find_element(*AF_Details.Owner_County).send_keys('Kent')
        driver.find_element(*AF_Details.Owner_Postcode).send_keys('TN23EF')
        FoundUs = driver.find_element(*AF_Details.Owner_FindUs)
        FoundUs.click()
        FoundUs.send_keys(Keys.ARROW_DOWN)
        FoundUs.send_keys(Keys.ENTER)
        driver.find_element(*AF_Details.ContinueButton).click()
    except:
        log("Failure to Generate")

def AnimalFriendsCat(driver, wait, dtrow):
    try:
        wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="details-section"]/div[1]/div[2]/div/label[2]')))
        driver.find_element(*AnimalFriendsAnimalType.Pet_Cat).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="details-section"]/div['
                                                               '2]/div/div[2]/div[1]/div/label[1]')))
        try:
            driver.find_element(*AF_PreExistingCons.PreConNo).click()
        except:
            log('PreCon Button not Found')
        try:
            wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="pet-details"]/div[1]/div[1]/div/label')))
        except:
            driver.find_element(*AF_PreExistingCons.PreConNo).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="pet-details"]/div[1]/div[1]/div/label')))
        driver.find_element(*AF_Details.Pet_Name).send_keys('Thomas')
        if 'Male' in dtrow[4]:
            driver.find_element(*AF_Details.Pet_Gender_Male).click()
        elif 'Female' in dtrow[4]:
            driver.find_element(*AF_Details.Pet_Gender_Female).click()
        petDob = BirthdayFromAge(dtrow[3])
        driver.find_element(*AF_Details.Pet_DoB).send_keys(petDob.strftime('%d%m%Y'))
        if 'Moggie' in dtrow[2]:
            driver.find_element(*AF_Details.Pet_Breed_Mog).click()
        else:
            driver.find_element(*AF_Details.Cat_Breed_Pedigree).click()
            BreedName = driver.find_element(*AF_Details.Cat_Breed_Selection)
            BreedName.send_keys(dtrow[2])
            BreedName.send_keys(Keys.ENTER)
        if 'Free' in dtrow[6]:
            driver.find_element(*AF_Details.Cat_Free).click()
        else:
            driver.find_element(*AF_Details.Cat_Paid_Btn).click()
            time.sleep(1)
            driver.find_element(*AF_Details.Cat_Paid_txt).send_keys(dtrow[6])
        driver.find_element(*AF_Details.Cat_NeverInsured).click()
        driver.find_element(*AF_Details.Cat_AccidentNo).click()
        driver.find_element(*AF_Details.Cat_NotDeclinedInsurance).click()
        driver.find_element(*AF_Details.Owner_FirstName).send_keys('Testing')
        driver.find_element(*AF_Details.Owner_LastName).send_keys('Testing')
        driver.find_element(*AF_Details.Owner_Email).send_keys('Test@test.com')
        driver.find_element(*AF_Details.Owner_Phone).send_keys('07814973804')
        driver.find_element(*AF_Details.Owner_DoB).send_keys('15121991')
        wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="client-details"]/div[5]/div[3]/span[2]')))
        driver.find_element(*AF_Details.Owner_ManualAddressBtn).click()
        driver.find_element(*AF_Details.Owner_Address_1).send_keys('unit 4')
        driver.find_element(*AF_Details.Owner_Address_2).send_keys('Chapman Way')
        driver.find_element(*AF_Details.Owner_Town).send_keys('Tunbridge Wells')
        driver.find_element(*AF_Details.Owner_County).send_keys('Kent')
        driver.find_element(*AF_Details.Owner_Postcode).send_keys('TN23EF')
        FoundUs = driver.find_element(*AF_Details.Owner_FindUs)
        FoundUs.click()
        FoundUs.send_keys(Keys.ARROW_DOWN)
        FoundUs.send_keys(Keys.ENTER)
        driver.find_element(*AF_Details.ContinueButton).click()

    except:
        log("Failure to Generate")

def AnimalFriendsDog(driver, wait, dtrow):
    try:
        wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="details-section"]/div[1]/div[2]/div/label[2]')))
        if 'Cat' in dtrow[1]:
            driver.find_element(*AnimalFriendsAnimalType.Pet_Cat).click()
        elif 'Dog' in dtrow[1]:
            driver.find_element(*AnimalFriendsAnimalType.Pet_Dog).click()
        time.sleep(1)
        wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="details-section"]/div['
                                                           '2]/div/div[2]/div[1]/div/label[1]')))
    #time.sleep(3)
        try:
            driver.find_element(*AF_PreExistingCons.PreConNo).click()
        except:
            log('PreCon Button not Found')
        try:
            wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="pet-details"]/div[1]/div[1]/div/label')))
        except:
            driver.find_element(*AF_PreExistingCons.PreConNo).click()
        wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="pet-details"]/div[1]/div[1]/div/label')))
        driver.find_element(*AF_Details.Pet_Name).send_keys('Thomas')
        if 'Male' in dtrow[4]:
            driver.find_element(*AF_Details.Pet_Gender_Male).click()
        elif 'Female' in dtrow[4]:
            driver.find_element(*AF_Details.Pet_Gender_Female).click()
        petDob = BirthdayFromAge(dtrow[3])
        driver.find_element(*AF_Details.Pet_DoB).send_keys(petDob.strftime('%d%m%Y'))
        if 'Dog' in dtrow[1]:
            if 'Crossbreed' in dtrow[2]:
                driver.find_element(*AF_Details.Pet_Breed_Mixed).click()
                if 'Small' in dtrow[2]:
                    driver.find_element(*AF_Details.Pet_Breed_Small).click()
                elif 'Medium' in dtrow[2]:
                    driver.find_element(*AF_Details.Pet_Breed_Medium).click()
                elif 'Large' in dtrow[2]:
                    driver.find_element(*AF_Details.Pet_Breed_Large).click()
            else:
                driver.find_element(*AF_Details.Pet_Breed_Pedigree).click()
                BreedName = driver.find_element(*AF_Details.Pet_Breed_Selection)
                BreedName.send_keys(dtrow[2])
                BreedName.send_keys(Keys.ENTER)
        if 'Crossbreed' in dtrow[2]:
            driver.find_element(*AF_Details.Mix_Free).click()
            driver.find_element(*AF_Details.Mix_NeverInsured).click()
            driver.find_element(*AF_Details.Mix_AccidentNo).click()
            driver.find_element(*AF_Details.Mix_NotDeclinedInsurance).click()
        else:
            if 'Free' in dtrow[6]:
                driver.find_element(*AF_Details.Pet_Free).click()
            else:
                driver.find_element(*AF_Details.Dog_Paid_Btn).click()
                driver.find_element(*AF_Details.Dog_Paid_txt).send_keys(dtrow[6])
            driver.find_element(*AF_Details.Pet_NeverInsured).click()
            driver.find_element(*AF_Details.Pet_AccidentNo).click()
            driver.find_element(*AF_Details.Pet_NotDeclinedInsurance).click()
        driver.find_element(*AF_Details.Owner_FirstName).send_keys('Testing')
        driver.find_element(*AF_Details.Owner_LastName).send_keys('Testing')
        driver.find_element(*AF_Details.Owner_Email).send_keys('Test@test.com')
        driver.find_element(*AF_Details.Owner_Phone).send_keys('07814973804')
        driver.find_element(*AF_Details.Owner_DoB).send_keys('15121991')
        wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="client-details"]/div[5]/div[3]/span[2]')))
        driver.find_element(*AF_Details.Owner_ManualAddressBtn).click()
        driver.find_element(*AF_Details.Owner_Address_1).send_keys('unit 4')
        driver.find_element(*AF_Details.Owner_Address_2).send_keys('Chapman Way')
        driver.find_element(*AF_Details.Owner_Town).send_keys('Tunbridge Wells')
        driver.find_element(*AF_Details.Owner_County).send_keys('Kent')
        driver.find_element(*AF_Details.Owner_Postcode).send_keys('TN23EF')
        FoundUs = driver.find_element(*AF_Details.Owner_FindUs)
        FoundUs.click()
        FoundUs.send_keys(Keys.ARROW_DOWN)
        FoundUs.send_keys(Keys.ENTER)
        driver.find_element(*AF_Details.ContinueButton).click()
    except:
        log('There was an Error')

def AnimalFriendsQuotePage(driver, wait, csv_writer, dtrow):
    wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="quote-section-content"]/div[2]/div/div/'
                                                           'div[1]/div[3]/div[1]/div/label[1]')))
    driver.find_element(*AF_QuoteType.AccidentAndIllness).click()
    driver.find_element(*AF_QuoteType.AI_LongTerm).click()
    driver.find_element(*AF_QuoteType.AI_1000_Button).click()
    LongTermMonth1000 = driver.find_element(*AF_QuoteType.AI_LT_1000_TopMonthly).text
    LongTermAnnual1000 =driver.find_element(*AF_QuoteType.AI_LT_1000_TopYearly).text
    LongTermAnnual1000 = LongTermAnnual1000.replace('or', '').replace('annually', '')
    LongTermVetExcess = driver.find_element(*AF_QuoteType.AI_LT_1000_VetExcess).text
    row = dtrow[0], dtrow[1], dtrow[2], dtrow[3], dtrow[4], dtrow[5], dtrow[6], LongTermMonth1000, LongTermAnnual1000.strip(), LongTermVetExcess, "1000"
    csv_writer.writerow(row)
    LongTermMonth2000 = driver.find_element(*AF_QuoteType.AI_LT_2000_TopMonthly).text
    LongTermAnnual2000 =driver.find_element(*AF_QuoteType.AI_LT_2000_TopYearly).text
    LongTermAnnual2000 = LongTermAnnual2000.replace('or', '').replace('annually', '')
    LongTermVetExcess = driver.find_element(*AF_QuoteType.AI_LT_2000_VetExcess).text
    row = dtrow[0], dtrow[1], dtrow[2], dtrow[3], dtrow[4], dtrow[5], dtrow[6], LongTermMonth2000, LongTermAnnual2000.strip(), LongTermVetExcess, "2000"
    csv_writer.writerow(row)
    LongTermMonth4000 = driver.find_element(*AF_QuoteType.AI_LT_4000_TopMonthly).text
    LongTermAnnual4000 =driver.find_element(*AF_QuoteType.AI_LT_4000_TopYearly).text
    LongTermAnnual4000 = LongTermAnnual4000.replace('or', '').replace('annually', '')
    LongTermVetExcess = driver.find_element(*AF_QuoteType.AI_LT_4000_VetExcess).text
    row = dtrow[0], dtrow[1], dtrow[2], dtrow[3], dtrow[4], dtrow[5], dtrow[6], LongTermMonth4000, LongTermAnnual4000.strip(), LongTermVetExcess, "4000"
    csv_writer.writerow(row)
    try:
        LongTermMonth6000 = driver.find_element(*AF_QuoteType.AI_LT_6000_TopMonthly).text
        LongTermAnnual6000 = driver.find_element(*AF_QuoteType.AI_LT_6000_TopYearly).text
        LongTermAnnual6000 = LongTermAnnual6000.replace('or', '').replace('annually', '')
        LongTermVetExcess = driver.find_element(*AF_QuoteType.AI_LT_6000_VetExcess).text
        row = dtrow[0], dtrow[1], dtrow[2], dtrow[3], dtrow[4], dtrow[5], dtrow[6], LongTermMonth6000, LongTermAnnual6000.strip(), LongTermVetExcess, "6000"
        csv_writer.writerow(row)
    except:
        row = dtrow[0], dtrow[1], dtrow[2], dtrow[3], dtrow[4], dtrow[5], dtrow[6], 'failed to extract', 'failed to extract', 'failed to extract', "6000"
        csv_writer.writerow(row)


def PetPlanPetDetails(driver, wait, dtrow):
    try:
        time.sleep(2)
        wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="petTypeDogLabel[0]"]')))
        if 'Dog' in dtrow[1]:
            driver.find_element(*PetPlan_PetDetails.btn_Dog).click()
        else:
            driver.find_element(*PetPlan_PetDetails.btn_Cat).click()
        driver.find_element(*PetPlan_PetDetails.txt_PetName).clear()
        driver.find_element(*PetPlan_PetDetails.txt_PetName).send_keys('Tommy')
        if 'Male' in dtrow[4]:
            driver.find_element(*PetPlan_PetDetails.btn_Male).click()
        else:
            driver.find_element(*PetPlan_PetDetails.btn_Female).click()
        if 'Yes' in dtrow[5]:
            driver.find_element(*PetPlan_PetDetails.btn_Neutered_Yes).click()
        else:
            driver.find_element(*PetPlan_PetDetails.btn_Neutered_No).click()
        driver.find_element(*PetPlan_PetDetails.btn_PreviouslyInjured_No).click()
        if 'Dog' in dtrow[1]:
            if 'Small' in dtrow[2]:
                driver.find_element(*PetPlan_PetDetails.btn_Dog_Mixed).click()
            elif 'Medium' in dtrow[2]:
                driver.find_element(*PetPlan_PetDetails.btn_Dog_Mixed).click()
            elif 'Large' in dtrow[2]:
                driver.find_element(*PetPlan_PetDetails.btn_Dog_Mixed).click()
            else:
                driver.find_element(*PetPlan_PetDetails.btn_Dog_Pedigree).click()
        if 'Small' in dtrow[2]:
            driver.find_element(*PetPlan_PetDetails.btn_Dog_Mixed_Small).click()
        elif 'Medium' in dtrow[2]:
            driver.find_element(*PetPlan_PetDetails.btn_Dog_Mixed_Medium).click()
        elif 'Large' in dtrow[2]:
            driver.find_element(*PetPlan_PetDetails.btn_Dog_Mixed_Large).click()
        else:
            if 'Dog' in dtrow[1]:
                wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="pedigreeBreed[0]"]')))
                driver.find_element(*PetPlan_PetDetails.txt_Dog_Breed).clear()
                driver.find_element(*PetPlan_PetDetails.txt_Dog_Breed).send_keys(dtrow[2])
            else:
                if 'Moggie' in dtrow[2]:
                    driver.find_element(*PetPlan_PetDetails.txt_Cat_Breed).clear()
                    driver.find_element(*PetPlan_PetDetails.txt_Cat_Breed).send_keys('Moggy')
                else:
                    driver.find_element(*PetPlan_PetDetails.txt_Cat_Breed).clear()
                    driver.find_element(*PetPlan_PetDetails.txt_Cat_Breed).send_keys(dtrow[2])
        petDob = BirthdayFromAge(dtrow[3])
        Day = str(petDob.strftime('%d'))
        if Day.startswith('0'):
            Day = Day.replace('0', '')
        Month = str(petDob.strftime('%m'))
        if Month.startswith('0'):
            Month = Month.replace('0', '')
        Year = str(petDob.strftime('%Y'))
        selectDay = Select(driver.find_element(*PetPlan_PetDetails.Select_Day))
        selectMonth = Select(driver.find_element(*PetPlan_PetDetails.Select_Month))
        selectYear = Select(driver.find_element(*PetPlan_PetDetails.Select_Year))
        selectYear.select_by_value('number:'+Year)
        selectMonth.select_by_value('number:'+Month)
        selectDay.select_by_value(Day)
        if 'Dog' in dtrow[1]:
            driver.find_element(*PetPlan_PetDetails.check_Dog_Behaviour).click()
            driver.find_element(*PetPlan_PetDetails.check_Dog_Attack).click()
            driver.find_element(*PetPlan_PetDetails.check_Dog_Guard).click()
            driver.find_element(*PetPlan_PetDetails.check_Dog_Alcohol).click()
            driver.find_element(*PetPlan_PetDetails.check_Dog_NoWork).click()
            driver.find_element(*PetPlan_PetDetails.btn_Dog_Continue).click()
            try:
                wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="title"]')))
            except:
                driver.find_element(*PetPlan_PetDetails.check_Dog_Behaviour).click()
                driver.find_element(*PetPlan_PetDetails.check_Dog_Attack).click()
                driver.find_element(*PetPlan_PetDetails.check_Dog_Guard).click()
                driver.find_element(*PetPlan_PetDetails.check_Dog_Alcohol).click()
                driver.find_element(*PetPlan_PetDetails.check_Dog_NoWork).click()
                driver.find_element(*PetPlan_PetDetails.btn_Dog_Continue).click()
        else:
            driver.find_element(*PetPlan_PetDetails.btn_Dog_Continue).click()


    except:
        print("Failure on details page")
        log("Failure to Generate")

def PetPlan_OwnerDetailsPage(driver, wait):
    try:
        wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="title"]')))
        selectTitle = Select(driver.find_element(*PetPlan_OwnerDetails.Select_Title))
        selectTitle.select_by_value("string:Mr")
        driver.find_element(*PetPlan_OwnerDetails.txt_FirstName).clear()
        driver.find_element(*PetPlan_OwnerDetails.txt_FirstName).send_keys('Testing')
        driver.find_element(*PetPlan_OwnerDetails.txt_Surname).clear()
        driver.find_element(*PetPlan_OwnerDetails.txt_Surname).send_keys('Test')
        selectDay = Select(driver.find_element(*PetPlan_OwnerDetails.Select_Day))
        selectDay.select_by_value('12')
        selectMonth = Select(driver.find_element(*PetPlan_OwnerDetails.Select_Month))
        selectMonth.select_by_value('number:6')
        selectYear = Select(driver.find_element(*PetPlan_OwnerDetails.Select_Year))
        selectYear.select_by_value('number:1991')
        driver.find_element(*PetPlan_OwnerDetails.txt_PhoneNumber).clear()
        driver.find_element(*PetPlan_OwnerDetails.txt_PhoneNumber).send_keys('07814973804')
        driver.find_element(*PetPlan_OwnerDetails.txt_Email).clear()
        driver.find_element(*PetPlan_OwnerDetails.txt_Email).send_keys('Test@test.com')
        driver.find_element(*PetPlan_OwnerDetails.txt_Postcode).clear()
        driver.find_element(*PetPlan_OwnerDetails.txt_Postcode).send_keys('tn23ef')
        driver.find_element(*PetPlan_OwnerDetails.btn_FindAddress).click()
        try:
            time.sleep(2)
            wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="addressList"]')))
            selectAddress = Select(driver.find_element(*PetPlan_OwnerDetails.Select_Address))
            selectAddress.select_by_visible_text('Vision Track,Unit 2 Chapman Way Tunbridge Wells')
        except:
            driver.find_element(*PetPlan_OwnerDetails.txt_HouseNumber).send_keys('Unit 2')
            driver.find_element(*PetPlan_OwnerDetails.txt_Street).send_keys('Chapman Way')
            driver.find_element(*PetPlan_OwnerDetails.txt_Town).send_keys('Tunbridge Wells')
            driver.find_element(*PetPlan_OwnerDetails.txt_County).send_keys('Kent')
        wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="skipnav"]/div[1]/div/div/div/div/form/section[3]/div/div[3]/button')))
        time.sleep(3)
        driver.find_element(*PetPlan_OwnerDetails.btn_OwnerContinue).click()
    except:
        log('Failed Owner Details Page')

def PetPlan_QuotePage(driver, wait, csv_writer, dtrow):
    try:
        time.sleep(2)
        wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="coveredForLifeBtn"]')))
        driver.find_element(*PetPlan_Quote.btn_Ongoing).click()
        time.sleep(3)
        wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="selectProduct"]/section[2]/div[2]/div/div[1]/div/div[1]/h2')))
        LongTerm4000Monthly = driver.find_element(*PetPlan_Quote.out_4000_Month).text
        LongTerm4000Annual = driver.find_element(*PetPlan_Quote.out_4000_Annual).text.replace('per month\n', '').replace('a year', '')
        LongTerm4000VetFees = driver.find_element(*PetPlan_Quote.out_4000_VetFees).text
        #LongTerm4000Annual = LongTerm4000Annual.replace('per month', '')
        row = dtrow[0], dtrow[1], dtrow[2], dtrow[3], dtrow[4], dtrow[5], dtrow[6], LongTerm4000Monthly, LongTerm4000Annual, LongTerm4000VetFees, "4000"
        csv_writer.writerow(row)
        print(LongTerm4000Annual)
        LongTerm7000Monthly = driver.find_element(*PetPlan_Quote.out_7000_Month).text
        LongTerm7000Annual = driver.find_element(*PetPlan_Quote.out_7000_Annual).text.replace('per month\n', '').replace('a year', '')
        LongTerm7000VetFees = driver.find_element(*PetPlan_Quote.out_7000_VetFees).text
        #LongTerm7000Annual = LongTerm7000Annual.replace('per month', '').replace(' a year').replace('\n','')
        row = dtrow[0], dtrow[1], dtrow[2], dtrow[3], dtrow[4], dtrow[5], dtrow[6], LongTerm7000Monthly, LongTerm7000Annual, LongTerm7000VetFees, "7000"
        csv_writer.writerow(row)
        LongTerm12000Monthly = driver.find_element(*PetPlan_Quote.out_12000_Month).text
        LongTerm12000Annual = driver.find_element(*PetPlan_Quote.out_12000_Annual).text.replace('per month\n', '').replace('a year', '')
        LongTerm12000VetFees = driver.find_element(*PetPlan_Quote.out_12000_VetFees).text
        #LongTerm12000Annual = LongTerm12000Annual.replace('per month', '').replace(' a year').replace('\n','')
        row = dtrow[0], dtrow[1], dtrow[2], dtrow[3], dtrow[4], dtrow[5], dtrow[6], LongTerm12000Monthly, LongTerm12000Annual, LongTerm12000VetFees, "4000"
        csv_writer.writerow(row)

    except:
        row = dtrow[0], dtrow[1], dtrow[2], dtrow[3], dtrow[4], dtrow[5], dtrow[6], 'No Lifetime Cover', 'No Lifetime Cover', 'No Lifetime Cover', "4000"
        csv_writer.writerow(row)
        row = dtrow[0], dtrow[1], dtrow[2], dtrow[3], dtrow[4], dtrow[5], dtrow[6], 'No Lifetime Cover', 'No Lifetime Cover', 'No Lifetime Cover', "7000"
        csv_writer.writerow(row)
        row = dtrow[0], dtrow[1], dtrow[2], dtrow[3], dtrow[4], dtrow[5], dtrow[6], 'No Lifetime Cover', 'No Lifetime Cover', 'No Lifetime Cover', "12000"
        csv_writer.writerow(row)


def AnimalFriendsCover(driver, wait, csv_writer, dtrow):
    wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="quote-section-content"]/div[2]/div/div/'
                                                           'div[1]/div[3]/div[1]/div/label[1]')))
    driver.find_element(*AF_QuoteType.AccidentOnly).click()
    wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="select-pet-cover-accident"]')))
    accidentOnlyMonthly = driver.find_element(*AF_QuoteType.AccidentMonthlyPrice).text
    accidentOnlyYearly = driver.find_element(*AF_QuoteType.AccidentYearlyPrice).text
    accidentOnlyYearly = accidentOnlyYearly.replace('or', '').replace('annually', '')
    row = dtrow[0], dtrow[1], dtrow[2], dtrow[3], dtrow[4], dtrow[5], accidentOnlyMonthly, accidentOnlyYearly.strip(), 'Accident Only'
    csv_writer.writerow(row)
    driver.find_element(*AF_QuoteType.AccidentAndIllness).click()
    driver.find_element(*AF_QuoteType.AI_ShortTermButton).click()
    driver.find_element(*AF_QuoteType.AI_1000_Button).click()
    aiShortTerm1000 = driver.find_element(*AF_QuoteType.AI_ST_1000_TopMonthly).text
    aiShortTerm1000Annual = driver.find_element(*AF_QuoteType.AI_ST_1000_TopYearly).text
    aiShortTerm1000Annual = aiShortTerm1000Annual.replace('or', '').replace('annually', '')
    row = dtrow[0], dtrow[1], dtrow[2], dtrow[3], dtrow[4], dtrow[5], aiShortTerm1000, aiShortTerm1000Annual.strip(),'Accident and Illness'
    csv_writer.writerow(row)
    print(row)



def TescoPetPage(driver, wait, dtrow):
    try:
        driver.find_element_by_xpath('//*[@id="ensCloseBanner"]').click()
    except:
        print("Didnt Need To Close Cookie Bar")
    log('Entering Pet Information')
    petName = driver.find_element(*DetailsPageLocators.Pet_Name)
    petName.send_keys('Tommy')
    driver.find_element(*DetailsPageLocators.Pet_Type).click()
    driver.find_element(*DetailsPageLocators.Pet_Type).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="dogPedigree0"]')))
    driver.find_element(*DetailsPageLocators.Pet_Breed_Pedigree).click()
    wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="predictiveTextBreedSelector0"]')))
    driver.find_element(*DetailsPageLocators.Pet_Breed_Name).send_keys('Black Mouth Cur')
    time.sleep(2)
    driver.find_element(*DetailsPageLocators.Pet_Breed_Name).send_keys(Keys.ARROW_DOWN)
    time.sleep(2)
    driver.find_element(*DetailsPageLocators.Pet_Breed_Name).send_keys(Keys.ENTER)
    driver.find_element(*DetailsPageLocators.Pet_Gender_Male).click()
    driver.find_element(*DetailsPageLocators.Pet_Gender_Male).click()
    driver.find_element(*DetailsPageLocators.Pet_DoB_Day).send_keys('21')
    driver.find_element(*DetailsPageLocators.Pet_DoB_Month).send_keys('06')
    driver.find_element(*DetailsPageLocators.Pet_DoB_Year).send_keys('2011')
    driver.find_element(*DetailsPageLocators.Pet_Price).send_keys('1000')
    driver.find_element(*DetailsPageLocators.Pet_N_or_S_No).click()
    driver.find_element(*DetailsPageLocators.Pet_Chipped_No).click()
    driver.find_element(*DetailsPageLocators.Pet_Legal_Action_No).click()
    driver.find_element(*DetailsPageLocators.Pet_Complaints_No).click()
    driver.find_element(*DetailsPageLocators.Pet_Home_Yes).click()
    driver.find_element(*DetailsPageLocators.Pet_Good_Health).click()
    log('Entering Owner Information')
    driver.find_element(*AboutYouLocators.Owner_Title).send_keys('Mr')
    driver.find_element(*AboutYouLocators.Owner_Title).send_keys(Keys.ENTER)
    driver.find_element(*AboutYouLocators.Owner_FirstName).send_keys('John')
    driver.find_element(*AboutYouLocators.Owner_Surname).send_keys('Smith')
    driver.find_element(*AboutYouLocators.Owner_DoB_Day).send_keys('20')
    driver.find_element(*AboutYouLocators.Owner_DoB_Month).send_keys('06')
    driver.find_element(*AboutYouLocators.Owner_DoB_Year).send_keys('1991')
    driver.find_element(*AboutYouLocators.Owner_EmailAddress).send_keys("Testing@markertsudy.com")
    driver.find_element(*AboutYouLocators.Owner_Phone_Number).send_keys('01323725776')
    driver.find_element(*AboutYouLocators.Owner_Marital_Status).send_keys('Married')
    driver.find_element(*AboutYouLocators.Owner_Marital_Status).send_keys(Keys.ENTER)
    driver.find_element(*AboutYouLocators.Owner_Postcode).send_keys('TN2 3EF')
    driver.find_element(*AboutYouLocators.Owner_FindAddress).click()
    wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="yourDetailsAddressIncorrectButton"]')))
    driver.find_element(*AboutYouLocators.Owner_EnterAddress).click()
    wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="yourDetailsManualAddressHouseNumber"]')))
    driver.find_element(*AboutYouLocators.Owner_ManualPostcode).send_keys('TN2 3EF')
    driver.find_element(*AboutYouLocators.Owner_HouseNumber).send_keys('4')
    driver.find_element(*AboutYouLocators.Owner_Street).send_keys('Chapman Way')
    driver.find_element(*AboutYouLocators.Owner_Town).send_keys('Tunbridge Wells')
    wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="yourDetailsManualAddressCountrySelectBoxItText"]')))
    driver.find_element(*AboutYouLocators.Owner_County).click()
    driver.find_element(*AboutYouLocators.Owner_County_Kent).click()
    #driver.find_element(*AboutYouLocators.Owner_County).send_keys(Keys.ENTER)
    driver.find_element(*AboutYouLocators.Owner_1_Pet).click()
    driver.find_element(*AboutYouLocators.Owner_Informed_No).click()
    #driver.find_element(*DetailsPageLocators.Pet_Breed_Name).send_keys('Black Mouth Cur')
    driver.find_element(*AboutYouLocators.Owner_Get_Quote).click()

def TescoYourQuote(driver, wait, csv_writer, dtrow):
    log('Collecting Quote Data')
    wait.until(ec.invisibility_of_element((By.XPATH, '//*[@id="yourDetailsPolicyHolderReferralSelectBoxIt"]')))
    wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="yourQuoteHide1"]/div[1]/div')))
    driver.find_element(*QuotePageLocators.Quote_Accident_Only).click()
    time.sleep(1)
    AccidentOnlyMonthlyQuote = driver.find_element(*QuotePageLocators.Quote_AO_Monthly)
    TescoAOMonthly = AccidentOnlyMonthlyQuote.text
    log('Tesco Accident Only Monthly is ' + TescoAOMonthly)
    AccidentOnlyYearlyQuote = driver.find_element(*QuotePageLocators.Quote_AO_Yearly)
    TescoAOYearly = AccidentOnlyYearlyQuote.text
    log('Tesco Accident Only Yearliy is ' + TescoAOYearly)
    row = 'Tesco', 'Dog', TescoAOMonthly, TescoAOYearly, 'Accident Only'
    csv_writer.writerow(row)
    driver.find_element(*QuotePageLocators.Quote_Accident_and_Illness).click()
    wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="iddEnhancedTile"]/div[3]/div[2]/fieldset/div/label[1]')))
    driver.find_element(*QuotePageLocators.Quote_AI_ShortTermOnly).click()
    wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="totalPriceText"]/span')))
    TescoAIMonthly = driver.find_element(*QuotePageLocators.Quote_AI_ShortTermOnly_Monthly).text
    TescoAIYearly = driver.find_element(*QuotePageLocators.Quote_AI_ShortTermOnly_Yearly).text
    row = 'Tesco', 'Dog', TescoAIMonthly, TescoAIYearly, 'Accident and Illness - Short Term'
    csv_writer.writerow(row)
    driver.find_element(*QuotePageLocators.Quote_AI_Ongoing).click()
    time.sleep(3)
    TescoAI_OngogingMonthly = driver.find_element(*QuotePageLocators.Quote_AI_Ongoing_Extra_Monthly).text
    TescoAI_OngoingYearly = driver.find_element(*QuotePageLocators.Quote_AI_Ongoing_Extra_Yearly).text
    row = 'Tesco', 'Dog', TescoAI_OngogingMonthly, TescoAI_OngoingYearly, 'Accident and Illness - Ongoing (Extra)'
    csv_writer.writerow(row)
    TescoPremierMonthly = driver.find_element(*QuotePageLocators.Quote_AI_Ongoing_Premier_Monthly).text
    TescoPremierYearly = driver.find_element(*QuotePageLocators.Quote_AI_Ongoing_Premier_Yearly).text
    row = 'Tesco', 'Dog', TescoPremierMonthly, TescoPremierYearly, 'Accident and Illness - Ongoing Premier'
    csv_writer.writerow(row)
