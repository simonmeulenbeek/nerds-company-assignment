import os
import tempfile

import pytest

from auth_server import create_app
from auth_server.db import get_db, initialize_database

with open(os.path.join(os.path.dirname(__file__), 'testdata.sql'), 'rb') as f:
    testdata = f.read().decode('utf8')

@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()
    app = create_app({
        'TESTING': True,
        'DATABASE': db_path
        })
    with app.app_context():
        initialize_database()
        get_db().executescript(testdata)
    yield app
    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    return app.test_client()