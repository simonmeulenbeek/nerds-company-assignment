import json
import base64
import datetime

from flask import ( 
    Blueprint, abort, request, session, redirect
)

from auth_server.db import get_db

blueprint = Blueprint('token', __name__)

@blueprint.route('/token', methods=['POST'])
def get_token():
    error = None
    data = request.data
    print(data)
    if len(data) == 0:
        error = 'No request-data!'
    else:
        parsed = json.loads(data)
        client_id = parsed.get('client_id', None)
        client_secret = parsed.get('client_secret', None)
        if client_id is None:
            error = 'Client_id is required!'
        else:
            client_obj = get_db().execute(
                'SELECT * FROM client WHERE client_id = ?', (client_id,)
            ).fetchone()
            if client_obj is None:
                error = 'Unknown client_id'
            else:
                secret = client_obj['client_secret']
                if secret != parsed['client_secret']:
                    error = 'Wrong secret'
    
    if error is None:
        return create_token(client_id, client_secret)
    return error


def create_token(client_id, client_secret):
    token = client_id + client_secret
    refresh = client_id + client_secret + 'refresh'
    token_hash = str(base64.b64encode(token.encode('utf8')))
    refresh_hash = str(base64.b64encode(refresh.encode('utf8')))
    json = {
        "access_token": token_hash,
        "token_type": 'bearer',
        "expires_in": 3600,
        "refresh_token": refresh_hash,
        "scope": '',
    }
    get_db().execute(
        'INSERT INTO token(access_token, token_type, expires_in, refresh_token, scope) VALUES (?, ?, ?, ?, ?)', (token_hash, 'bearer', '3600', refresh_hash, '')
    )
    return json