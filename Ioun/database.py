__author__ = 'Alec Nunn'
import sqlite3

def get_db():
    return sqlite3.connect('ioun.db', isolation_level=None)

def init_db():
    import os
    import common
    try:
        os.remove('ioun.db')
        db = get_db()
        db.executescript(common.init_sql)
        db.close()
    except:
        pass


def query(q, args=(), one=False):
    """
    Queries the DB and returns list of lists
    """
    cur = get_db().execute(q, args)
    r = cur.fetchall()
    return (r[0] if r else None) if one else r

def get_pages():
    return query('select title from pages')

def get_page(title):
    return query('select title, subtitle, body from pages where title=?', [title], one=True)

def create_page(title):
    query('insert into pages (title) values (?)', [title], one=True)
    return query('select title, subtitle, body from pages where title=?', [title], one=True)

def save_page(contents=()):
    return query('update pages set title=?, subtitle=?, body=? where title=?', [contents[0].replace(' ', '_'), contents[1], contents[2], contents[0].replace(' ', '_')])