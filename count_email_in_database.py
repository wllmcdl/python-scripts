import sqlite3

db = sqlite3.connect('emaildb.sqlite')
cur = db.cursor()

cur.execute('''drop table if exists counts''')
cur.execute('''create table counts (email text, count integer)''')

fl = open('mbox.txt')

for line in fl:
    if not line.startswith('From'): continue
    places = line.split()
    email = places[1]
    cur.execute('select count from counts where email = ?', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('insert into counts (email, count) values(?,1)', (email,))
    else:
        cur.execute('update counts set count = count = 1 where email = ?', (email,))
    db.commit()

sql = 'select email, count from counts order by count desc limit 10'

for row in cur.execute(sql):
    print(str(row[0]), str(row[1]))
