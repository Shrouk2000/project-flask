from flask_sqlalchemy import SQLAlchemy
import os

class Config:
    SECRET_KEY = os.urandom(32)

    @staticmethod
    def init_app(app):
        pass
class Devconfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI="sqlite:///database.db"
   
class Prodconfig(Config):
    
    DEBUG=False
    SQLALCHEMY_DATABASE_URI= 'postgresql://fayoum:iti@localhost:5432/postlab3'
    UPLOADED_PHOTOS_DEST = 'app/static/'
    
config_option={
        'dev':Devconfig,
        'prd':Prodconfig
    }

