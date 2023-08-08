import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_data(url):

    response = requests.get(url)

    soup = BeautifulSoup(response.content,'html.parser')

    product_names = soup.find_all('div', {'class': '_4rR01T'})


    product_prices = soup.find_all('div',{'class':'_30jeq3 _1_WHN1'})

    product_ratings = soup.find_all('div',{'class':'_3LWZlK'})

    data = dict(names=[name.text for name in product_names],
                prices=[price.text for price in product_prices])
                # ratings=[rating.text for rating in product_ratings])

    df = pd.DataFrame(data,index=list(range(len(product_names))))

    df.to_csv('flipkart.csv',mode='a')

    return response

if __name__ == '__main__':
    url = 'https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
    print(get_data(url))