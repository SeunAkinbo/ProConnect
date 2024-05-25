#!/usr/bin/python3
class Config:
    MYSQL_HOST = '127.0.0.1'
    MYSQL_USER = 'pro_dev'
    MYSQL_PASSWORD = 'pro_dev_pwd'
    MYSQL_DB = 'pro_dev_db'
    
    # SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
