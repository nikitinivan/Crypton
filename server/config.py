import os


class Configuration:
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    DEBUG = True
    SECRET_KEY = 'thisissecretkeyforcrypton' # change it in production !!!
    MONGO_DBNAME = 'cryptondb'
