import sqlite3
# DB Browser for sqlite
db = sqlite3.connect('training.db')
cur = db.cursor()
cur.execute('create table book(id int, title varchar(20))')

