'''
Hint: The top organizational count is 536.
This application will read the mailbox data (mbox.txt) and count the number of email messages per organization (i.e. domain name of the email address)
'''

import sqlite3, re, os

db = sqlite3.connect('emaildb.sqlite')
cursor = db.cursor()
cursor.execute('''DROP TABLE IF EXISTS counts''')
cursor.execute('''CREATE TABLE counts (org TEXT, count INTEGER)''')

os.chdir('/Users/william/Code/python/python_course')
fl = open('mbox.txt')
count = 0
for line in fl:
    if not line.startswith('From '): continue
    places = line.split()
    email = places[1]
    obj = re.search(r'@([a-zA-Z0-9.-_]+\.[a-z]+)', email)
    domain = obj.group(1)

    if domain == 'iupui.edu':
        count += 1

    cursor.execute('SELECT count FROM counts WHERE org = ?', (domain,))
    # This method returns only one record, If there are no more records then it returns None.
    row = cursor.fetchone()
    if row is None:
        cursor.execute('INSERT INTO counts (org, count) VALUES(?,1)', (domain,))
    else:
        cursor.execute('UPDATE counts SET count = count + 1 WHERE org = ?', (domain,))

db.commit()

sql = 'SELECT org, count FROM counts ORDER BY count DESC LIMIT 5'
for row in cursor.execute(sql):
    print(str(row[0]), str(int(row[1])))

print(count)