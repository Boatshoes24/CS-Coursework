# Name: Wade Moulton
# Date: 10/11/2020
# Class: CS 4720
# Section: W01
# Instructor: Dr. Sarah North
# Assignment_4-Database

import sqlite3
from os.path import join, split


# supplied function from lecture slides
def dictionary_factory(cursor, row):
    col_names = [d[0].lower() for d in cursor.description]
    return dict(zip(col_names, row))


# supplied function from lecture slides
def getConnection():
    this_dir = split(__file__)[0]
    fname = join(this_dir, 'sqlite-sakila.sq')
    conn = sqlite3.connect(fname)
    conn.row_factory = dictionary_factory
    return conn


# supplied function from lecture slides
def do_command(cmd, args=[]):
    try:
        conn = getConnection()
        crs = conn.cursor()
        crs.execute(cmd, args)
        return crs.fetchall()
    finally:
        conn.close()

