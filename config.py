import os

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

SECRET_KEY = 'development key'

# dev
FLASK_DEBUG = True
# prod
FLASK_DEBUG = False

app.config['TESTING'] = True

SECRET_KEY = os.urandom(16)

_mail_enabled = os.environ.get("MAIL_ENABLED", default="true")
MAIL_ENABLED = _mail_enabled.lower() in {"1", "t", "true"}

SECRET_KEY = os.environ.get("SECRET_KEY") or os.urandom(16)

if not SECRET_KEY:
    raise ValueError("No SECRET_KEY set for Flask application")