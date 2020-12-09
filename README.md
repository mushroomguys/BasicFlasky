# Flask - project
***
This is a project that condensate the flask framework and the main geospatial software such as QGIS, Geoserver and PostgreSQL.

## Description of the parts

<!--

# url_for / inside template file / return function's route

# request / HTTP methods = access URLs

# static files / Web server serve us these files at PROD

# url_for generation / url_for('static', filename='style.css')

# Jinja2 / template engine / Combinbaison html and python

# render_template / method to render an HTML template

# If app is inside a module / If app is inside a package

# {% block %} from Base template are overridable by Child template

# template have access to / request, session and g objects and get_flashed_messages() method

# Template inheritence / Keep some constant like header between several pages

# Markup class / URL pass VARIABLE to the template and TEMPLATE mark the variable as SAFE ?

# Request / Request Global Object / Flask / threadsafe / context locals (implement tests ) ?

# Python 'Requests' != Flask 'Request' module (from flask import request)

# File Uploads / Filesystem / server / client

# Cookies / Cookies Attribute = request.cookies.xxxx / dictionnary of cookies transmited by client

# Cookies / views / return / string / convert / response object / make_response() function

# Cookies / Set cookies before response object = before return statement / in a view / ?

# Sessions / add security on top of cookies

# Redirects and Errors / abort(), redirect() functions / ...

# errorhandler() decorator / to customize the error page

# About Responses / OK !

# APIs with JSON / OK !

# Message Flashing / flash() method ==> feedback to the user after a request

# WSGI ?

# Using Flask Extensions / ex. Flask-SQLAlchemy provides SQLAlchemy 

# Deploying to a Web Server

-->

$ escape() ?

### Project organization

<!-- 
/home/user/Projects/flask-tutorial
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── venv/
├── setup.py
└── MANIFEST.in
 -->