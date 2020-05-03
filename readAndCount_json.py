# access this json read it and sum the values
import urllib.request
import urllib.parse
import urllib.error
import json

url = 'http://py4e-data.dr-chuck.net/comments_483697.json'
connection = urllib.request.urlopen(url)
html = connection.read().decode()

count = 0
data = json.loads(html)['comments']

for item in data:
    count = count + int(item['count'])

print(count)