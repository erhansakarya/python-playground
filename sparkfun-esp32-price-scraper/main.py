import requests
from bs4 import BeautifulSoup

getResponseForEsp32 = requests.get('https://www.sparkfun.com/search/results_framework?term=esp32', timeout=10)
#print(getResponseForEsp32)

soup = BeautifulSoup(getResponseForEsp32.text, 'lxml')

# find total product count
productCount = soup.find(href='#products')
print("total product count: " + str(productCount['data-total']))

# find product names
productNames = soup.find_all(name='h3', class_="title")
for productName in productNames:
    print('\n' + productName.a.text + productName.a.get('href'))
    getProductPage = requests.get(productName.a.get('href'), timeout=10)
    soup = BeautifulSoup(getProductPage.text, 'lxml')
    productPrice = soup.find(class_='price')
    for child in productPrice.findChildren():
        print(child.text, end='')