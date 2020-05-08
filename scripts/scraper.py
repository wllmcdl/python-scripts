import requests
from bs4 import BeautifulSoup
import json
import csv

'''With Python's requests (pip install requests) library we're getting a web page by 
using get() on the URL. The response r contains many things, but using r.content will 
give us the HTML. Once we have the HTML we can then parse it for the data we're 
interested in analyzing.'''

url = 'https://www.worten.pt/informatica-e-acessorios/computadores/computadores-portateis-marca-apple-e-dell-e-lenovo?per_page=24&page=1'

html = requests.get(url)
soup = BeautifulSoup(html.content, 'lxml')

csv_file = open('scrape.csv', 'w')
csv_writer = csv.writer(csv_file)

csv_writer.writerow(['image', 'description', 'price'])

cat = list()

for product in soup.find_all(class_='w-product__wrapper'):
    description = product.find(class_='w-product__title').text
    price = product.find(class_='w-product-price__main').text + ',' + product.find(class_='w-product-price__dec').text
    try:
        image = product.find('figure', class_='w-product__image').img['data-src']
        image = f'https://worten.pt/{image}'
    except:
        image = None
    
    dic = {'description':description,'price':price,'image':image}
    cat.append(dic)
    print(description)
    csv_writer.writerow([image, description, price])


with open('scrape.json', 'w') as f:
    json.dump(cat, f, indent=4)
    pass
