import os
import re
from flask import Flask, jsonify, render_template, request

from cs50 import SQL
from helpers import lookup

import feedparser
import urllib.parse
from urllib.parse import unquote
# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///mashup.db")

# Feedparser url to geo = https://news.google.com/news/local/section/geo/02138
entry = {}
entry1 = []

geo = "02138"
s = feedparser.parse("https://news.google.com/news/rss/local/section/geo/02138")

for r in range(5):
    entry["link"] = s.entries[r].link
    entry["title"] = s.entries[r].title

    print(f"{entry}")
    entry1.append(entry.copy())
s = "New%20Haven"
result = urllib.parse.unquote(s)
print(f"{result}")


# Url parse %20
q = urllib.parse.unquote("New%20Haven%20CT")



# https://www.geeksforgeeks.org/python-string-split/ # Splits at space
qa = q.split()

# Splits at ','
qb = q.split()

# Tests which one can be used
if qa:

    # Text len
    z = len(qa)

    # Check if z == 3
    if z == 3:

        # Where has three opptions
        qw = db.execute("SELECT * FROM places WHERE place_name = :qa1 and admin_name1 = :qa2 and admin_code1 = :qa3", qa1=qa[0], qa2=qa[1], qa3=qa[2])

    # Check if z == 2
    elif z == 2:

        # Where has two opptions
        qw = db.execute("SELECT * FROM places WHERE place_name = :qa1 and admin_name1 = :qa2", qa1=qa[0], qa2=qa[1])

    # If z == 1
    else:

        # Where has one opptions
        qw = db.execute("SELECT * FROM places WHERE place_name = :qa1", qa1=qa[0])

# Else qb not NULL can be choosed of doning selecting
if qb:

    # Test len
    z1 = len(qb)

    # Check if z == 3
    if z1 == 3:

        # Where has three opptions
        qw1 = db.execute("SELECT * FROM places WHERE place_name = :qb1 and admin_name1 = :qb2 and admin_code1 = :qb3", qb1=qb[0], qb2=qb[1], qb3=qb[2])

    # Check if z == 2
    elif z1 == 2:

        # Where has two opptions
        qw1 = db.execute("SELECT * FROM places WHERE place_name = :qb1 and admin_name1 = :qb2", qb1=qb[0], qb2=qb[1])

    # If z == 1
    else:

        # Where has one opptions
        qw1 = db.execute("SELECT * FROM places WHERE place_name = :qb1", qb1=qb[0])

# https://www.geeksforgeeks.org/python-string-split/ # Splits at space
qc = q.split()

# Nessary to check here after will be changed
z3 = len(qc)


if z3 > 1:

    # Tran
    qc[0] = qc[0] +" "+ qc[1]





# Splits at ','
qd = q.split()

# Nessary to check here after will be changed
z4 = len(qd)


if z4 > 1:

    # Tran
    qd[0] = qd[0]+" " + qd[1]



# Tests which one can be used
if qc:

    # Text len
    z = len(qc)

    # Check if z == 3
    if z == 3:

        # Where has three opptions
        qw2 = db.execute("SELECT * FROM places WHERE place_name = :qc1 and admin_name1 = :qc2 and admin_code1 = :qc3", qc1=qc[0], qc2=qc[1], qc3=qc[2])

    # Check if z == 2
    elif z == 2:

        # Where has two opptions
        qw2 = db.execute("SELECT * FROM places WHERE place_name = :qc1 and admin_name1 = :qc2", qc1=qc[0], qc2=qc[1])

    # If z == 1
    else:

        # Where has one opptions
        qw2 = db.execute("SELECT * FROM places WHERE place_name = :qc1", qc1=qc[0])

# Else qd not NULL can be choosed of doning selecting
if qd:

    # Test len
    z1 = len(qd)

    # Check if z == 3
    if z1 == 3:

        # Where has three opptions
        qw3 = db.execute("SELECT * FROM places WHERE place_name = :qd1 and admin_name1 = :qd2 and admin_code1 = :qd3", qd1=qd[0], qd2=qd[1], qd3=qd[2])

    # Check if z == 2
    elif z1 == 2:

        # Where has two opptions
        qw3 = db.execute("SELECT * FROM places WHERE place_name = :qd1 and admin_name1 = :qd2", qd1=qd[0], qd2=qd[1])

    # If z == 1
    else:

        # Where has one opptions
        qw3 = db.execute("SELECT * FROM places WHERE place_name = :qd1", qd1=qd[0])


CREATE TABLE 'places' ('country_code' char(2) NOT NULL, 'postal_code' varchar(20) NOT NULL, 'place_name' varchar(180) NOT NULL, 'admin_name1' varchar(100) NOT NULL, 'admin_code1' varchar(20) NOT NULL, 'admin_name2' varchar(100) NOT NULL, 'admin_code2' varchar(20) NOT NULL, 'admin_name3' varchar(100) NOT NULL, 'admin_code3' varchar(20) NOT NULL, 'latitude' double precision NOT NULL, 'longitude' double precision NOT NULL, 'accuracy' integer NOT NULL)
print(f"{qw}")
print(f"{qw1}")
print(f"{qw2}")
print(f"{qw3}")