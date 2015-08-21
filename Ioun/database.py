__author__ = 'Alec Nunn'
import sqlite3


def get_db():
    """
    Connects to the database and returns the database object.
    We set the isolation level to None so that all queries are automatically
    committed/saved.
    """
    return sqlite3.connect('ioun.db', isolation_level=None)


def init_db():
    """
    Initializes the database.  If the database file (ioun.db) already exists
    the file is deleted.  The database is then "connected" to and the init_sql
    script from common is executed.
    """
    import os
    import common
    if os.path.isfile('ioun.db'):
        os.remove('ioun.db')
    db = get_db()
    db.executescript(common.init_sql)
    db.close()


def query(q, args=(), one=False):
    """
    Queries the DB and returns list of lists
    Based on sample code from Flask
    """
    cur = get_db().execute(q, args)
    r = cur.fetchall()
    return (r[0] if r else None) if one else r


def get_pages():
    """
    Queries the database and returns a list of every page consisting of
    the page names
    """
    return query('select title from pages where visible=1')


def get_page(title):
    """
    Queries the database and returns the contents of an individual page
    """
    return query('select title, subtitle, body, visible from pages where title=?', [title], one=True)


def create_page(title):
    """
    Inserts a new page into the database with simply the title.  After
    the page is created, we can then worry about filling in the other
    fields
    """
    query('insert into pages (title) values (?)', [title], one=True)
    return query('select title, subtitle, body from pages where title=?', [title], one=True)


def save_page(contents=()):
    """
    Updates an existing entry in the database with a tuple of values.
    """
    return query('update pages set title=?, subtitle=?, body=?, visible=? where title=?', [contents[0].replace(' ', '_'), contents[1], contents[2], contents[3], contents[0].replace(' ', '_')])


def delete_page(title):
    """
    Deletes a page from the database
    """
    return query('delete from pages where title=?', [title], one=True)