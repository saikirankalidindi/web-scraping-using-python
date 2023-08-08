from bs4 import BeautifulSoup
import requests

def get_page(url):

    response = requests.get(url)

    content = response.content.decode('utf-8')

    soup = BeautifulSoup(content,'html.parser')

    return soup.prettify()

url = 'https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'

print(get_page(url))