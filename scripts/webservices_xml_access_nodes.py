import xml.etree.ElementTree as et

data = '''
<person>
    <name>Chuck</name>
    <phone type="intl">+ 351 917 828 342</phone>
    <email hide="yes"/>
</person>
'''

tree = et.fromstring(data)

print('Name:', tree.find('name').text) # /person/name/chuck
print('Attr:', tree.find('email').get('hide')) # /person/email/hide/yes
print('Phone:', tree.find('phone').get('type')) # /person/phone/type/intl  get the attr value
print('Phone:', tree.find('phone').text)  # /person/phone/+ 351 917 828 342 get the tag value



'''
tree representation
          <name> - "Chuck"
        / 
<person> - <phone> - (type) = "intl"
        \           \
          \           "+351 917 828 342"
            \
              <email> - (hide) = "yes"

it can be represented as paths too:
/person/name = Chuch
/person/phone = +351 917 828 342
/person/phone(type) = intl
/person/email(hide) = yes

obs: 
-> type and hide are attributes
-> chuck is a text content
-> email is a self closing tag
'''
