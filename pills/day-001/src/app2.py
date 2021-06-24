from flask import Flask
import logging

app = Flask(__name__)
logging.basicConfig(filename='app.log',level=logging.DEBUG)

@app.route("/")
def hello():
    app.logger.info('Main request successfull')
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)