'''
Sample data: http: // py4e-data.dr-chuck.net/comments_42.xml(Sum=2553)
Actual data: http: // py4e-data.dr-chuck.net/comments_483696.xml(Sum ends with 28)
'''
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as et
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_483696.xml'
html = urllib.request.urlopen(url).read()
# print(html.decode())
tree = et.fromstring(html)
lst = tree.findall('comments/comment')
count = 0
for item in lst:
    count = count + int((item.find('count').text))
print(count)
