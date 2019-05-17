import os
import re
from flask import Flask, jsonify, render_template, request

from cs50 import SQL
from helpers import lookup

import feedparser
import urllib.parse
import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from pytz import timezone
from urllib.parse import unquote

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///mashup.db")

s = "Cambridge"
result = urllib.parse.unquote(s)
q = result
z = db.execute("SELECT * FROM places WHERE place_name = :q" and admin_name1 = , q=q)
print(f"{result}")
zo = len(z)
print(f"{zo}")



