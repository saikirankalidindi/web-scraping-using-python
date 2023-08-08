from selenium import webdriver
from pymongo import MongoClient
from selenium.webdriver.common.by import By

client = MongoClient('mongodb://localhost:27017/')

database = client['phones']
collection = database['iphones']

driver = webdriver.Chrome()

driver.get('https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')

prices = driver.find_elements(By.CSS_SELECTOR,'._30jeq3._1_WHN1')

names = driver.find_elements(By.CSS_SELECTOR,'._4rR01T')

ratings = driver.find_elements(By.CSS_SELECTOR,'._3LWZlK')

product_names = [name.text for name in names]

product_prices = [price.text for price in prices]

product_ratings = [rating.text for rating in ratings]

data = {'product_names':product_names,'product_prices':product_prices,'product_ratings':product_ratings}

data = list(zip(product_names,product_prices,product_ratings))
for i in range(len(data)):

    collection.insert_one({'product_name':data[i][0],'product_price':data[i][1],
                        'product_rating':data[i][2]})

print('inserted successfully.')