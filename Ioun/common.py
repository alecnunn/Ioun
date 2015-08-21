"""
Common strings used throughout the entire program.  I will try to
keep the longer blocks of text and strings in here simply to keep
the other code files clean.
"""

__author__ = 'Alec Nunn'
__version__ = '1.0'

init_sql = """create table 'pages' (
    'id' integer primary key autoincrement,
    'title' varchar(50) unique,
    'subtitle' varchar(50),
    'body' text,
    'visible' integer
);
"""

help_txt = """Ioun is a simple wiki software written in Python.
Ioun is currently on version {0}
To use Ioun, simply run the `ioun` executable
Available options:
 -h / --help    : Print out this help message
 -i / --init    : Initializes the database [*]
 -v / --version : Print out current version of Ioun

[*] Initializing the database, but it will wipe your current database""".format(__version__)