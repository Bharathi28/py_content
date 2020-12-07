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
        driver = webdriver.Chrome(executable_path=r"F:\Python\GR\Driver\chromedriver.exe")
        script_dir = os.path.dirname(__file__)

        abs_file_path = os.path.join(script_dir, rel_path)
        print(abs_file_path)
        p = Path(__file__).parents[2]
        print(os.path.join(p, rel_path))
        # driver.maximize_window()
        # driver.get(URL)

driver.quit()
