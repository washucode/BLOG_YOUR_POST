import os
basedir = os.path.abspath(os.path.dirname(__file__))
# base dir = os.path.returns an absolute path (os.path.returns directory name)
class Config(object):
     # DEBUG = True   
     DEBUG = False
     TESTING = False
     QOUTESAPI = 'http://quotes.stormconsultancy.co.uk/random.json'
     SECRET_KEY = '435313ea80b5a872114356a1'
     SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
     UPLOADED_PHOTOS_DEST ='app/static/photos'
    
     

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


config_options = {
'test':TestingConfig
}
