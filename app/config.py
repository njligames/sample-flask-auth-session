# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os
from   decouple import config

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():

    CSRF_ENABLED = True

    # Set up the App SECRET_KEY
    SECRET_KEY = config('SECRET_KEY', default=os.environ["SECRET_KEY"])
    PASSWORD = config('PASSWORD', default=os.environ["PASSWORD"])
    PUBLIC_IP_ADDRESS = config('PUBLIC_IP_ADDRESS', default=os.environ["PUBLIC_IP_ADDRESS"])
    DBNAME = config('DBNAME', default=os.environ["DBNAME"])
    PROJECT_ID = config('PROJECT_ID', default=os.environ["PROJECT_ID"])
    INSTANCE_NAME = config('INSTANCE_NAME', default=os.environ["INSTANCE_NAME"])

    db_user="root"
    db_pass=PASSWORD
    db_name=DBNAME
    address=PUBLIC_IP_ADDRESS
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqldb://{db_user}:\'{db_pass}\'@{address}/{db_name}"

    # This will create a file in <app> FOLDER
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
    # SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket=/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}".format(PASSWORD=PASSWORD, PUBLIC_IP_ADDRESS=PUBLIC_IP_ADDRESS, DBNAME=DBNAME, PROJECT_ID=PROJECT_ID, INSTANCE_NAME=INSTANCE_NAME)
    # SQLALCHEMY_DATABASE_URI = "mysql + mysqldb://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket=/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}".format(PASSWORD=PASSWORD, PUBLIC_IP_ADDRESS=PUBLIC_IP_ADDRESS, DBNAME=DBNAME, PROJECT_ID=PROJECT_ID, INSTANCE_NAME=INSTANCE_NAME)

    SQLALCHEMY_TRACK_MODIFICATIONS = False
