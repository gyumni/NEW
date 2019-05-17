import os
import re
from flask import Flask, jsonify, render_template, request

from cs50 import SQL
from helpers import lookup

import feedparser
import urllib.parse
# import pandas as pd

# Configure application
app = Flask(__name__)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///mashup.db")
s = 0
        s1 = 0
        # If A# URL(https://stackoverflow.com/questions/36977811/how-to-detect-non-ascii-character-in-python)
        for c in q:
            s = s + 1
            if 0 <= ord(c) <= 127:
                s1 = s1+1# this is a ascii character.
            else:
                del q[s-1]
                q.insert(s-1," ")

        # https://www.geeksforgeeks.org/python-string-split/ # Splits at space
        qa = q
        # .split()
        if len(qa)==2:



            # Query for two items
            rows = db.execute("SELECT * FROM places WHERE places MATCH ':qa*' ", qa=qa)
        elif len(qa)==1:
            # Query for two items
            rows = db.execute("SELECT * FROM places WHERE places MATCH :qa", qa=qa+"*")
        else:
            # Query for two items
            rows = db.execute("SELECT * FROM places WHERE places MATCH ':qa*' ", qa=qa)



            return jsonify(rows)