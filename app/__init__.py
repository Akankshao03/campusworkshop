"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi87lrhp8u7g2ei24tg-a.oregon-postgres.render.com",
        database="todo_3oxl",
        user="betsol",
        password="wAFtNAxegDKLl3WzQ4Ynm6ZugfQZ4xDQ")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
