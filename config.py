import os

class Config:
    SECRET_KEY = 'supersecretkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///erp.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
