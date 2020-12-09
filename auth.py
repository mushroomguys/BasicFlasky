import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from BasicFlasky.db import get_db

bp_auth = Blueprint('auth', __name__, url_prefix='/auth')

@bp_auth.route('/login')
def register():
    return render_template('auth/login.html')

@bp_auth.route('/register')
def register():
    return render_template('auth/register.html')

@bp_auth.route('/logout')
def logout():
	return redirect(url_for('index'))