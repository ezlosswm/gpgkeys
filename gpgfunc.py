#!/usr/bin/env python3

import sqlite3 as db
from datetime import datetime

DATE = str(datetime.now())

# Initializes the data base 
def init():
    conn = db.connect("gpgkeys.db")
    cur = conn.cursor()
    sql = '''
    create table if not exists gpgkeys (
        gpg_key string,
        repo string,
        time string
    )
    '''

    cur.execute(sql)
    conn.commit()

# Logs the user input 
def log(gpg_key, repo_name):
    conn = db.connect("gpgkeys.db")
    cur = conn.cursor()
    
    sql = '''
    insert into gpgkeys values (
        '{}',
        '{}',
        '{}'
    )
    '''.format(gpg_key, repo_name, DATE)

    cur.execute(sql)
    conn.commit()

# Prints the database 
def view(repo_name=None):
    conn = db.connect("gpgkeys.db")
    cur = conn.cursor()
    if repo_name:

        sql = '''
        select * from gpgkeys
        '''.format(repo_name)
    else:
        sql = '''
        select * from gpgkeys
        '''.format(repo_name)

    cur.execute(sql)
    results = cur.fetchall()

    return results


