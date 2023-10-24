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

    db_user="root"
    db_pass=config('PASSWORD', default=os.environ["PASSWORD"])
    db_name=config('DBNAME', default=os.environ["DBNAME"])
    db_host=config('PUBLIC_IP_ADDRESS', default=os.environ["PUBLIC_IP_ADDRESS"])
    db_port=3306
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqldb://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
