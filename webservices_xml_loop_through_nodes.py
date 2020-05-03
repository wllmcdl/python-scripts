import xml.etree.ElementTree as et

data = '''
<stuff>
    <users>
        <user x = "2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x = "7">
            <id>009</id>
            <name>William</name>
        </user>
    </users>
</stuff>
'''

stuff = et.fromstring(data)
lst = stuff.findall('users/user')

for item in lst:
    print('Attribute: ', item.get('x'))
    print('Id: ', item.find('id').text)
    print('Name: ', item.find('name').text)