from flask import g, session

from setuptests import app, client

def test_login_happy_flow(client):
    with client:
        response = client.post('/login', data={'username': 'testuser', 'password': 'testpassword'}, follow_redirects=True)
        assert '200' in response.status
        print(response)
        print(session)
        client.get('/')
        print(session)
        assert session.get('user_id') == 'testuser'

def test_login_wrong_username(client):
    with client:
        response = client.post('/login', data={'username': 'testuser1', 'password': 'testpassword'}, follow_redirects=True)
        client.get('/')
        assert b'Incorrect user' in response.data
        assert session.get('user_id') == None

def test_login_wrong_password(client):
    with client:
        response = client.post('/login', data={'username': 'testuser', 'password': 'wrongpassword'}, follow_redirects=True)
        client.get('/')
        assert b'Incorrect password' in response.data
        assert session.get('user_id') == None