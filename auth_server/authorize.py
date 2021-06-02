import json
import base64
import datetime

from flask import ( 
    Blueprint, abort, request, session, redirect
)

from auth_server.db import get_db
from auth_server.login import login_required

blueprint = Blueprint('authorize', __name__)

@blueprint.route('/authorize', methods=['GET'])
@login_required
def authorize():
    user = session.get('user_id', None)
    if user is None:
        error = 'Not logged in!'

    data = request.data
    error = None
    if len(data) == 0:
        error = 'No JSON data!'
    else:    
        parsed = json.loads(data)
        client_id = parsed.get('client_id', None)
        if client_id is None:
            error = 'Need client_id'
        else:
            db = get_db()
            client = db.execute(
                'SELECT * FROM client WHERE client_id = ?', (client_id,)
            ).fetchone()
            if client is None:
                error = 'No client found for client_id'
            else:
                redirect_uri = parsed.get('redirect_uri', client['redirect_uri'])
                if redirect_uri is None or redirect_uri == '':
                    error = 'Can\'t find redirect URI!'
    
    if error is None:
        code = create_auth_code(user, client_id, redirect_uri).decode('utf8')
        return redirect(redirect_uri + "?code=" + code)
    else:
        return error

def create_auth_code(user_id, client_id, redirect_uri):
    string = user_id + client_id + redirect_uri
    hash = base64.b64encode(string.encode('utf8'))
    expiration = datetime.datetime.now() + datetime.timedelta(0, 300)
    get_db().execute(
        'INSERT INTO authcode(code, client_id, username, expiration) VALUES (?, ?, ?, ?)', (hash, client_id, user_id, expiration)
    )
    return hash