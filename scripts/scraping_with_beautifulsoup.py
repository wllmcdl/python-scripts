'''
BeautifulSoup 
Is a library for extracting data from HTML and XML files. It is particularly useful in that it does not require the source markup to be well-formed. For example, it deals with missing tags and incorrect nesting as smoothly as possible.

Urllib 
Is a library for open, reading, and parsing URLs
'''

'''
This program opens an url read it with urllib and then parse it using BeautifulSoup. After that, it will find all of the span tags, grap their value and then sum them
'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

# url = input("Enter url: ")
url = 'http://py4e-data.dr-chuck.net/comments_483694.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

lst = list()
count = 0
tags = soup.find_all("span")
lst = re.findall('>([0-9]+?)<', str(tags))

for i in lst:
    count = count + int(i)

print(count)