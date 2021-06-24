# Simple Flask app

Follow this instructions to run the simple flash app.

## Prerequisites

You must have [Python 3+](https://www.python.org/downloads/) installed.

## Install dependencies

Just install the dependencies from `requirements.txt` file.

```bash
> pip install -r requirements.txt
```

> Optional: You could use virtualenv instead of install dependencies globally. Take a look here for [more](https://docs.python-guide.org/dev/virtualenvs/#:~:text=virtualenv%20is%20a%20tool%20to,standalone%2C%20in%20place%20of%20Pipenv.) info.

## Run using `flask run` - The preferred way to start the development server

Use the FLASK_APP environment variable to point the command at your app. Set FLASK_ENV=development to run with the debugger and reloader.

for MacOs and Linux users:

```bash
> export FLASK_APP=app
> export FLASK_ENV=development
> flask run
```

On Windows CMD, use set instead of export.

```bash
> set FLASK_APP=app
> set FLASK_ENV=development
> flask run
```

For PowerShell, use $env:

```bash
> $env:FLASK_APP = "app"
> $env:FLASK_APP = "development"
> flask run
```

## Run  `python app.py`

```bash
> python app.py
```

The `python app.py` command runs a Python file and sets __name__ == "__main__". The main block calls app.run(), and it will run the development server.

```python
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
```

> Never use this command to deploy publicly, use a production WSGI server such as Gunicorn, uWSGI, Waitress, or mod_wsgi.

> To run the app2.py just change the name from `app` to `app2`.