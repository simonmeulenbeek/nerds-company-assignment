from setuptests import app, client

def test_auth_happy_flow(client):
    with client:
        response = client.post('/login', data={'username': 'testuser', 'password': 'testpassword'}, follow_redirects=True)
        json = {"client_id": "poc-test-app"}
        response = client.get('/authorize', json=json)
        assert b'?code=' in response.data
        assert '302' in response.status

def test_auth_not_logged_in(client):
    with client:
        response = client.get('/authorize')
        assert '302' in response.status

def test_auth_loggedin_without_data(client):
    with client:
        response = client.post('/login', data={'username': 'testuser', 'password': 'testpassword'}, follow_redirects=True)
        response = client.get('/authorize')
        assert b'No JSON data!' in response.data 

def test_auth_loggedin_with_client_id(client):
    with client:
        response = client.post('/login', data={'username': 'testuser', 'password': 'testpassword'}, follow_redirects=True)
        json = {"client_id": "poc-test-app"}
        response = client.get('/authorize', json=json)
        assert b'?code=' in response.data
        assert '302' in response.status


def test_auth_loggedin_with_wrong_client_id(client):
    with client:
        response = client.post('/login', data={'username': 'testuser', 'password': 'testpassword'}, follow_redirects=True)
        json = {"client_id": "poc-test-app-wrong"}
        response = client.get('/authorize', json=json)
        assert b'No client found for client_id' in response.data
