import os
import configparser as ConfigParser

from flask import Flask
from flask import render_template
from flask import jsonify

def check_service():
    config = ConfigParser.ConfigParser()
    config.read('config.env')
    for addr in config.options('WHITE_LIST'):
        url = os.environ.get(addr)
        if url==None:
            url = config.get('WHITE_LIST', addr)

        print(url)


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # store the database in the instance folder
        # DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/home")
    def home():
        return render_template("home.html")

    @app.route("/healthz", methods=("GET", "POST"))
    def healthz():
        """Return K8s Liveness check."""
        resp = jsonify(success=True)
        resp.status_code = 200
        return resp

    # apply the blueprints to the app
    import handlers as handlers

    app.register_blueprint(handlers.bp)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule("/", endpoint="home")

    check_service()

    return app

if __name__ == '__main__':
    port = os.environ.get('PORT', "5000")
    create_app().run('0.0.0.0', port)