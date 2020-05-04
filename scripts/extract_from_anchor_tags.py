'''
Two files are provided for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment

Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah
Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Leea.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: M
'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
import ssl

# ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Leea.html'
# return the entire document as a single string with new lines at the end of each line
html = urllib.request.urlopen(url, context=ctx).read()
# return an object with a clean html
soup = BeautifulSoup(html, 'html.parser')
# retrieve all the a tags

lst = list()
tags = soup('a')
x = tags[17].get('href', None)
lst.append(url)
lst.append(x)

for i in range(6) :
    url = x
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    x = tags[17].get('href', None)
    lst.append(x)

for i in re.findall('known_by_([a-zA-Z]+?).html', str(lst)):
    print(i)