import json

from setuptests import app, client

def test_token_happy_flow(client):
    post_data = {
        'grant_type': 'authorization_code',
        'code': 'testcode',
        'redirect_uri': 'http://127.0.0.1:5001/',
        'client_id': 'poc-test-app',
        'client_secret': 'poc-test-secret'
    }
    response = client.post('/token', json=post_data)
    assert len(response.data) != 0
    print(response.data)
    json_response = json.loads(response.data)
    assert 'access_token' in json_response

def test_token_not_authorized(client):
    post_data = {
        'grant_type': 'authorization_code',
        'code': 'testcode',
        'redirect_uri': 'http://127.0.0.1:5001/',
        'client_id': 'poc-test-app',
        'client_secret': 'poc-test-secret-wrong'
    }
    response = client.post('/token', json=post_data)
    assert len(response.data) != 0
    assert b'Wrong secret' in response.data

def test_token_unknown_client(client):
    post_data = {
        'grant_type': 'authorization_code',
        'code': 'testcode',
        'redirect_uri': 'http://127.0.0.1:5001/',
        'client_id': 'poc-test-app-wrong',
        'client_secret': 'poc-test-secret'
    }
    response = client.post('/token', json=post_data)
    assert len(response.data) != 0
    assert b'Unknown client_id' in response.data
