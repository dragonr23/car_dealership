import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    #environ.get will look at the enviroment variables and see if the secret key is included. It will use that value if so.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_TRACK_MODIFICATIONS = False


    #uri for sql lite database

    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')

#uri for postgress database, connect to local twitter commerce database that we creates on pgAdmin

# 'postgresql://name_of_user:pass_for-user@domanin_address:port/name_of_db'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:0ceanP@rk@localhost:5432/car_dealership'
