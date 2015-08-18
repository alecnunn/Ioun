__author__ = 'Alec Nunn'


def init_db():
    import os
    try:
        os.remove('ioun.db')
    except:
        pass


def query(q, args=(), one=False):
    """
    Queries the DB and returns list of lists
    """
    cur = get_db().execute(q, args)
    r = cur.fetchall()
    return (r[0] if r else None) if one else r