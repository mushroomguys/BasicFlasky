from flask import Flask, render_template, url_for, session, request

def create_app(test_config=None):

    # instance_relative_config = to override configfile
    app = Flask(__name__, instance_relative_config=True)



	from . import main
	app.register_blueprint(auth.bp_main)

	from . import auth
	app.register_blueprint(auth.bp_auth)

    return app