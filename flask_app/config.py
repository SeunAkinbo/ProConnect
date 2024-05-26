#!/usr/bin/python3
class Config:
    SECRET_KEY = 'the-cow-jumped-over-the-moon'
    MYSQL_HOST = '18.234.105.208'
    MYSQL_USER = 'pro_dev'
    MYSQL_PASSWORD = 'pro_dev_pwd'
    MYSQL_DB = 'pro_dev_db'
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

