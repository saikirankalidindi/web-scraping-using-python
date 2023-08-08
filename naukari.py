from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient

driver = webdriver.Chrome()
url = 'https://www.naukri.com/it-jobs?src=gnbjobs_homepage_srch'
driver.get(url)
content = driver.page_source
client = MongoClient('mongodb://localhost:27017/')
database = client['naukari']
collection = database['jobs']

wait = WebDriverWait(driver,10)

roles = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,'a.title.ellipsis')))
job_roles = [role.text for role in roles]

experience = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,'span.ellipsis.fleft.expwdth')))
job_experience = [exp.text for exp in experience]

location = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,'span.ellipsis.fleft.locWdth')))
job_location = [sal.text for sal in location]

company = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,'a.subTitle.ellipsis.fleft')))
company_names = [name.text for name in company]

desc = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,'div.ellipsis.job-description')))
job_description = [des.text for des in desc]

data = list(zip(job_roles,job_experience,company_names,job_location,job_description))

for i in range(len(data)):
    collection.insert_one({'job_role':data[i][0],'job_experience':data[i][1],'company_name':data[i][2],
                           'job_location':data[i][3],'job_description':data[i][4]})
    
print('inserted.')

