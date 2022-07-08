#!/usr/bin/env python3

import sqlite3 as db
from datetime import datetime

DATE = str(datetime.now())

# Initializes the data base 
def init():
    conn = db.connect("gpgkeys.db")
    cur = conn.cursor()

    sql = '''
    CREATE TABLE IF NOT EXISTS gpgkeys (
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
    # data = (gpg_key, repo, DATE)
    
    sql = '''insert into gpgkeys values (
        '{}', '{}', '{}'
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
        select * from gpgkeys where repo = '{}'
        '''.format(repo_name)
    else:
        sql = '''
        select * from gpgkeys
        '''

    cur.execute(sql)
    results = cur.fetchall()

    

    return results

def delete(repo_name):
    conn = db.connect("gpgkeys.db")
    cur = conn.cursor()

    sql = '''
    delete from gpgkeys where repo = '{}'
    '''.format(repo_name)

    cur.execute(sql)
    conn.commit()