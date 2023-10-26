# [Flask User Authentication](https://blog.appseed.us/flask-user-authentication-free-sample/)

Open-source Flask project that implements a simple authentication system using `Flask-Login` library - Features:

- ✅ `Up-to-date dependencies`
- ✅ Authentication layer: `Flask-Login`
- ✅ UI: Bootstrap5 via `CDN`
- ✅ Free [Support](https://appseed.us/support/) via `Email` and `Discord`.

<br />

## TODO
How it should work.
The User goes to the main page. (rewordme.html)
The main page talks about what the site does and has the text area and button to reword the text.
They can also login or register on the page.

When they try to reword:  
    If the user is logged in then;  
        The rewording works and goes to the reword.html
    If the user is not logged in then;  
        The user is directed to the index.html page where they can either login or register.

When they try to register, they must purchase the subscription.

* [] - create the beginning rewordme.html
* [] - logic to determine if they have an account or not so that we know which way to redirect.
* [] - insert the copy code for copying the code


## Build from sources

> **Step #1** - Clone sources (this repo)

```bash
$ # Clone the sources
$ git clone https://github.com/app-generator/sample-flask-auth-session.git
$ cd sample-flask-auth-session
```

<br />

> **Step #2** - Create a virtual environment

```bash
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
```

<br />

> **Step #3** - Install dependencies

```bash
$ # Install requirements
$ pip3 install -r requirements.txt
```

<br />

> **Step #4** - Set Up Environment

```bash
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
```

<br />

> **Step #5** - Create Tables (SQLite persistance)

```bash
$ # Create tables
$ flask shell
$ >>> from app import db
$ >>> db.create_all()
```

<br />

> **Step #6** - (optional) Enable DEBUG Environment (local development)

```bash
$ # Set up the DEBUG environment
$ # (Unix/Mac) export FLASK_ENV=development
$ # (Windows) set FLASK_ENV=development
$ # (Powershell) $env:FLASK_ENV = "development"
```

<br />

> **Step #7** - Start the project

```bash
$ # Run the application
$ # --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
$ # --port=5000    - specify the app port (default 5000)  
$ flask run --host=0.0.0.0 --port=5000
$
$ # Access the app in browser: http://127.0.0.1:5000/
```

<br />

![Flask User Authentication - Free sample provided by AppSeed.](https://user-images.githubusercontent.com/51070104/134959525-3ad0c71c-27e4-45f7-b7b9-53b76f3884bf.png)

<br />

## Code-base structure

The project has a super simple structure, represented as bellow:

```bash
< PROJECT ROOT >
   |
   |-- app/
   |    |-- static/
   |    |    |-- <css, JS, images>    # CSS files, Javascripts files
   |    |
   |    |-- templates/
   |    |    |
   |    |    |-- index.html           # Index File
   |    |    |-- login.html           # Login Page
   |    |    |-- register.html        # Registration Page
   |    |    
   |    |
   |   config.py                      # Provides APP Configuration 
   |   forms.py                       # Defines Forms (login, register) 
   |   models.py                      # Defines app models 
   |   views.py                       # Application Routes 
   |
   |-- requirements.txt
   |-- run.py
   |
   |-- ************************************************************************
```

<br />

## Resources

- Free [Admin Dashboards](https://appseed.us/admin-dashboards/open-source) - index provided by AppSeed
- [Flask Social Login](https://blog.appseed.us/flask-social-login-with-github/) - blog article (includes a free sample)

<br />

---
[Flask User Authentication](https://blog.appseed.us/flask-user-authentication-free-sample/) - Free sample provided by **AppSeed**.
