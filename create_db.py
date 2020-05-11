# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 18:40:15 2020

@author: heman
"""

import sqlite3
from sqlite3 import Error

conn = sqlite3.connect('database.db')

if conn is not None:
    query =  """CREATE TABLE IF NOT EXISTS models (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        trained TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        metric INT NOT NULL);"""
    try:
        c = conn.cursor()
        c.execute(query)
    except Error as e:
        print(e)