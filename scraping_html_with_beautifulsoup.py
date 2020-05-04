import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup as beautify
import re

url = 'http://py4e-data.dr-chuck.net/comments_483694.html' # input('Enter -> ')
html = urllib.request.urlopen(url).read()
soup = beautify(html, 'html.parser')

lst = list()
count = 0
tags = soup.find_all('span')
lst = re.findall('>([0-9]+?)<', str(tags))

for i in range(len(lst)):
    count = count + int(lst[i])

print(count)