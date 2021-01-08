from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from CommonUtilities import my_function
from DB import db_connection as connect
from DB import get_url
from DB import get_cta_locators
import os
from pathlib import Path

# Read inputs from excel
# Env = QA, Brand = CrepeERase, Campaign = core

# url = get_url (env, brand, campaign)
rel_path = "Driver/chromedriver.exe"
data = my_function()
for x in data:
    print(x)
    if x[0] == "Environment":
        continue
    elif x[0] == "End":
        break
    else:
        env = x[0]
        brand = x[1]
        campaign = x[2]
        print("Execution started for " + env + brand + campaign)
        URL = get_url(env, brand, campaign)
        print(URL)
        p = Path(__file__).parents[2]
        print(os.path.join(p, rel_path))

        script_dir = os.path.dirname(__file__)
        abs_file_path = os.path.join(script_dir, rel_path)
        print(abs_file_path)
        p = Path(__file__).parents[2]
        path = os.path.join(p, rel_path)
        print(os.path.join(p, rel_path))

        driver = webdriver.Chrome(executable_path=path)
        driver.maximize_window()
        driver.get(URL)
        # Step 1 : Check - Terms & Conditions
        # Store all locators in content_locators table
        # Replicate get_element_locator function from CommonUtilities.java file
        print(driver.title)
        element = WebDriverWait(driver, 100).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Terms & Conditions')]")))
        TC = driver.find_element_by_xpath("//a[contains(text(),'Terms & Conditions')]")
        TC.click()
        TC1 = "//div[@id='popupcontent']"
        element = WebDriverWait(driver, 100).until(
            EC.visibility_of_element_located((By.XPATH, TC1)))
        element1 = driver.find_element_by_xpath("//div[@id='popupcontent']").text
        element2 = element1.rstrip()
        path = "F:\Python\GR\Content\Terms of Use and Conditions\English"
        path2 = path + "\\" + brand + ".txt"
        File2 = open(path2, "r")
        File1 = (File2.read())
        File1.rstrip()
        if element2 == File1:
            print("Terms of Use and Conditions of Purchase : " + "Passed")
        else:
            print("Terms of Use and Conditions of Purchase : " + "Failed")

driver.quit()
