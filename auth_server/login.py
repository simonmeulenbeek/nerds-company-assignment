import functools

from flask import ( 
    Blueprint, request, session, render_template, redirect, url_for, flash, g
)
from werkzeug.security import check_password_hash, generate_password_hash

from auth_server.db import get_db

blueprint = Blueprint('login', __name__)

@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()
        if user is None:
            error = 'Incorrect user'
        elif not user['password'] == password:
            error = 'Incorrect password'
        
        if error is None:
            session.clear()
            session['user_id'] = user['username']
            return redirect(url_for('home'))
        
        flash(error)
    
    return render_template('login.html')

@blueprint.before_app_request
def load_logged_in_user():
    username = session.get('user_id')
    if username is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('login.login'))

        return view(**kwargs)
    
    return wrapped_view
