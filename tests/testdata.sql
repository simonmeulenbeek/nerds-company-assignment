INSERT INTO user(username, password, roles, scopes)
VALUES 
    ('testuser', 'testpassword',  'role-1 role-2', 'scope1 scope2'),
    ('testadmin', 'adminpassword', 'adminrole', 'scope1 scope2 adminscope');

INSERT INTO client(client_id, client_secret, redirect_uri, scope, authorized_grant_types)
VALUES 
    ('poc-test-app', 'poc-test-secret', 'http://127.0.0.1:5001/', '', '');

INSERT INTO authcode(code, client_id, username, expiration)
VALUES ('testcode', 'poc-test-app', 'testuser', '2021-06-03 18:00:00.000000')