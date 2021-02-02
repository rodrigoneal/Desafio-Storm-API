"""inicia o flask e suas dependencias."""

from flask import Flask
from desafios.blueprints import init_app as bp_init_app

app = Flask(__name__)


def create_app():
    """
    Cria factory function que inicia  e passa o objeto Flask para suas dependencias.

    :return: object Flask
    """
    app.config["TESTING"] = True
    bp_init_app(app)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
