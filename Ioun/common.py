__author__ = 'Alec Nunn'
__version__ = '1.0'

init_sql = """
create table 'users' (
    'id' integer primary key autoincrement,
    'username' varchar(30),
    'password' text
);

create table 'categories' (
    'id' integer primary key autoincrement,
    'name' varchar(25)
);

create table 'pages' (
    'id' integer primary key autoincrement,
    'title' varchar(50),
    'body' text
);

insert into 'users' (
    'username',
    'password'
) VALUES (
    'admin',
    'pbkdf2:sha1:1000$p6oKPxJK$6e59d6338f1b44dcec1ead129d6238d1d3e6c206'
);

insert into 'categories' (
    'name'
) values (
    'Scripting'
);
"""

help_txt = """Ioun is a simple wiki software written in Python.
Ioun is currently on version {0}
To use Ioun, simply run the `ioun` executable
Available options:
 -h / --help    : Print out this help message
 -i / --init    : Initializes the database [1].
 -v / --version : Print out current version of Ioun

[1] Initializing the database, but it will wipe your current database.""".format(__version__)