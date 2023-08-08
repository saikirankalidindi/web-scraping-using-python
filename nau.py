from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient

driver = webdriver.Chrome()
url = 'https://www.naukri.com/it-jobs?src=gnbjobs_homepage_srch'
driver.get(url)
content = driver.page_source

soup = BeautifulSoup(content,'html.parser')

wait = WebDriverWait(driver,10)

skills = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,'li.fleft.dot')))

for skill in skills:
    print(skill.text)