__author__ = 'Tomas Kracka'
__version__ = 0.1

import logging

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello Adform'


@app.errorhandler(500)
def server_error(e):
    logging.exception("An error occurred during a request.")
    return """
    Internal error occurred <pre>{}</pre>
    See logs for full stacktrace
    """.format(e), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
