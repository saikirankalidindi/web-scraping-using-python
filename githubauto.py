from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()

driver.get('https://github.com/login')

time.sleep(5)
content = driver.page_source

soup = BeautifulSoup(content,'html.parser')

username = driver.find_element(By.ID,'login_field')
username.send_keys('username')

password = driver.find_element(By.ID,'password')
password.send_keys('password')

driver.find_element(By.XPATH,"//input[@type='submit' and @value='Sign in']").click()

profile_url = ''

driver.get(profile_url)

start = time.time()

# will be used in the while loop
initialScroll = 0
finalScroll = 1000

while True:
	driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
	
	initialScroll = finalScroll
	finalScroll += 1000
	time.sleep(10)
	end = time.time()
	if round(end - start) > 20:
		break

src = driver.page_source

soup = BeautifulSoup(src,'html.parser')

intro = soup.find('div',{'class':''})

