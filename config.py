import os
basedir = os.path.abspath(os.path.dirname(__file__))
# base dir = os.path.returns an absolute path (os.path.returns directory name)
class Config(object):
     # DEBUG = True   
     DEBUG = False
     TESTING = False
    
     

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
