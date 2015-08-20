__author__ = 'Alec Nunn'
__version__ = '1.0'

init_sql = """create table 'pages' (
    'id' integer primary key autoincrement,
    'title' varchar(50) unique,
    'subtitle' varchar(50),
    'body' text
);
"""

help_txt = """Ioun is a simple wiki software written in Python.
Ioun is currently on version {0}
To use Ioun, simply run the `ioun` executable
Available options:
 -h / --help    : Print out this help message
 -i / --init    : Initializes the database [1]
 -v / --version : Print out current version of Ioun
 -l / --license : Print out the license that Ioun is distributed under

[1] Initializing the database, but it will wipe your current database""".format(__version__)

license = 'Ioun is released under the LGPL license'