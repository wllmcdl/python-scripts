'''
BeautifulSoup 
Is a library for extracting data from HTML and XML files. It is particularly useful in that it does not require the source markup to be well-formed. For example, it deals with missing tags and incorrect nesting as smoothly as possible.

Urllib 
Is a library for open, read, and parsing URLs
'''

'''
Using urllib.request.urlopen() to open a website when crawling, and encounters “HTTP Error 403: Forbidden”. It possibly due to the server doesn't know the request is coming from. Some websites will verify the UserAgent in order to prevent from abnormal visit. So you should provide information of your fake browser visit.
'''

from bs4 import BeautifulSoup as beautify

import re
from urllib.request import urlopen, Request
import urllib.request
import urllib.parse, urllib.error

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
url = 'https://www.worten.pt/informatica-e-acessorios/computadores/computadores-portateis-marca-apple-e-dell-e-lenovo?per_page=48'
req = Request(url=url, headers=headers)
html = urlopen(req).read()
soup = beautify(html, 'html.parser')

cat = list()

# price = soup.find_all(attrs={"class": "w-currentPrice iss-current-price"})
price = soup.find_all('span', class_='w-currentPrice iss-current-price')
# description = soup.find_all(attrs={"class": "w-product__title"})
description = soup.find_all('h3', class_='w-product__title')

descrip = re.findall(r'>(.+?)</h3>', str(description))
prices = re.findall(r'class="w-product-price__main">([0-9]+?)<', str(price))
prices_dec = re.findall(
    r'class="w-product-price__dec">([0-9]{2})<', str(price))

'''
# Concatenate the price + comma + decimal parts through regex
for i in range(len(prices)):
    price = (str(prices[i]) + ',' + str(prices_dec[i]))
    dic = {'Description': descrip[i], 'Price': price}
    cat.append(dic)

for i in cat:
    print(i)
'''

# Concatenate the price + comma + decimal parts through regex
for i in range(len(prices)):
    group = re.search(
        r'class="w-product-price__main">([0-9]+?)<\/span>(,)<sup class="w-product-price__dec">([0-9]{2})', str(price[i]))
    x = (group.group(1) + group.group(2) + group.group(3))
    dic = {'Description': descrip[i], 'Price': x}
    cat.append(dic)

for i in cat:
    print(i)
