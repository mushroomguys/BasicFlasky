import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from BasicFlasky.db import get_db

bp_main = Blueprint('main', __name__, url_prefix='/auth')

@bp_main.route('/')
def register():
    return render_template('main/index.html')