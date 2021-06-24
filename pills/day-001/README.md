# Python daily pills - Day 001: What does `if __name__ == "__main__":` do?

For this pill, we'll use a simple [flask app](./src).

## Symptoms

Take a look in the `app.py` code:

```python
from flask import Flask
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info('Main request successfull') # logger been used
    return "Hello World!"

if __name__ == "__main__":
    logging.basicConfig(filename='app.log',level=logging.DEBUG) # logger been initialized
    app.run(host='0.0.0.0', debug=True)
```

If you use `flask run` to start your app the app.log file will not be created.

Instead, usign `python app.py` to start the app, the log file will be created.

## Remedy

To solve this issue in both app start strategies, one option is move `logging.basicConfig` out of the `if` statement as such:

```python
from flask import Flask
import logging

app = Flask(__name__)
logging.basicConfig(filename='app.log',level=logging.DEBUG) # <-- logger been initialized moved

@app.route("/")
def hello():
    app.logger.info('Main request successfull') # logger been used
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
```

## Explanation

When using `flask run` the app.py is loaded as module, and the if statement is evaluated as false.

## References

If you want more info about how main function works in python:

- A [realpython](https://realpython.com/python-main-function/) article
- A [stackoverflow](https://stackoverflow.com/questions/419163/what-does-if-name-main-do) thread
