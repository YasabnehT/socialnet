import os
from os import path
import sqlite3

root = os.path.dirname(path.relpath((__file__)))

def create_post(name, content):
    con = sqlite3.connect(path.join(root,'socialnet.db'))
    cur =con.cursor()
    cur.execute('insert into posts(name, content) values(?,?)', (name,content))
    con.commit()
    con.close()
def get_posts():
    con =sqlite3.connect(path.join(root, 'socialnet.db'))
    cur = con.cursor()
    cur.execute('select * from posts')
    posts = cur.fetchall()
    return posts
