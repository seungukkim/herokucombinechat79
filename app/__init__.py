import os 

from flask import Flask, render_template


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'development'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def hello():
        return render_template('index.jinja2', title='index page')

    from .main import main
    # from .dashapp1 import dashapp1
    from .dashapp1 import bp as bp_dashapp1
    from .dashapp1.dashapp1 import add_dash
    from .dashapp2 import dashapp2


    app.register_blueprint(main.bp)
    app.register_blueprint(bp_dashapp1)
    app.register_blueprint(dashapp2.bp)

    app = add_dash(app)

    return app
