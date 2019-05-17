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


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    """Render map"""
    return render_template("index.html")


@app.route("/articles")
def articles():
    """Look up articles for geo"""

    # Get geo for articles
    geo = request.args.get("geo")

    if not geo:
        return jsonify(False)
    else:

        # Feedparser url to geo = https://news.google.com/news/rss/local/section/geo/02138
        s = feedparser.parse(f"https://news.google.com/news/rss/local/section/geo/{geo}")

        entry = {}
        entry1 = []

        # Get five link and title of dict use .entries function
        for r in range(5):
            entry["link"] = s.entries[r].link
            entry["title"] = s.entries[r].title

            # Add new dict entry to entry1 list
            entry1.append(entry.copy())

    # Return json
    return jsonify(entry1)


@app.route("/search")
def search():
    """Search for places that match query"""

    # Get geo for articles
    qq = request.args.get("q")

    if not qq:
        return jsonify(False)
    else:
        # Url parse %20
        q = urllib.parse.unquote(qq)

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
        if len(qa)==1:



            # Query for two items
            rows = db.execute("SELECT * FROM places WHERE postal_code AND place_name OR admin_name1 MATCH :qa LIMIT 10 ", qa="^"+qa+"*")
        elif len(qa)==2:
            # Query for two items
            rows = db.execute("SELECT * FROM places WHERE places MATCH 'postal_code : :qa OR place_name : :qa OR admin_name1 : :qa'", qa=qa+"*")
        else:
            # Query for two items
            rows = db.execute("SELECT * FROM places WHERE places MATCH 'postal_code : A* OR place_name : A* OR admin_name1 : A*' ")



    return jsonify(rows)


@app.route("/update")
def update():
    """Find up to 10 places within view"""

    # Ensure parameters are present
    if not request.args.get("sw"):
        raise RuntimeError("missing sw")
    if not request.args.get("ne"):
        raise RuntimeError("missing ne")

    # Ensure parameters are in lat,lng format
    if not re.search("^-?\d+(?:\.\d+)?,-?\d+(?:\.\d+)?$", request.args.get("sw")):
        raise RuntimeError("invalid sw")
    if not re.search("^-?\d+(?:\.\d+)?,-?\d+(?:\.\d+)?$", request.args.get("ne")):
        raise RuntimeError("invalid ne")

    # Explode southwest corner into two variables
    sw_lat, sw_lng = map(float, request.args.get("sw").split(","))

    # Explode northeast corner into two variables
    ne_lat, ne_lng = map(float, request.args.get("ne").split(","))

    # Find 10 cities within view, pseudorandomly chosen if more within view
    if sw_lng <= ne_lng:

        # Doesn't cross the antimeridian
        rows = db.execute("""SELECT * FROM places
                          WHERE :sw_lat <= latitude AND latitude <= :ne_lat AND (:sw_lng <= longitude AND longitude <= :ne_lng)
                          GROUP BY country_code, place_name, admin_code1
                          ORDER BY RANDOM()
                          LIMIT 10""",
                          sw_lat=sw_lat, ne_lat=ne_lat, sw_lng=sw_lng, ne_lng=ne_lng)

    else:

        # Crosses the antimeridian
        rows = db.execute("""SELECT * FROM places
                          WHERE :sw_lat <= latitude AND latitude <= :ne_lat AND (:sw_lng <= longitude OR longitude <= :ne_lng)
                          GROUP BY country_code, place_name, admin_code1
                          ORDER BY RANDOM()
                          LIMIT 10""",
                          sw_lat=sw_lat, ne_lat=ne_lat, sw_lng=sw_lng, ne_lng=ne_lng)

    # Output places as JSON
    return jsonify(rows)
