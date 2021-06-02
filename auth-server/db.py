import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext

def connect_app(app):
    app.cli.add_command(init_db_commandline)
    app.teardown_appcontext(close_db)

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('db.sql')
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(E=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def initialize_database():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

@click.command('init-db')
@with_appcontext
def init_db_commandline():
    initialize_database()