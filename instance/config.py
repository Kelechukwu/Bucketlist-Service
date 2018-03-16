import os 

class Config(object):
    """Parent configuration class."""
    DEBUG=False
    CSRF_ENABLED =True
    SECRET_KEY = os.getenv('SECRET')

    # Without this get_auth_token via POST request w/ JSON data does not work
    # You keep getting "CSRF token missing" error
    WTF_CSRF_ENABLED = False

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_TRACKABLE = True
    SECURITY_PASSWORD_SALT = 'something_super_secret_change_in_production'

class DevelopementConfig(Config):
    """Configuration for Development"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://kc:admin@localhost/test_db'
    
class TestingConfig(Config):
    """Configuration for Testing"""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://kc:admin@localhost/test_db'

class StagingConfig(Config):
    """Configuration for Staging"""
    DEBUG = True

class ProductionConfig(Config):
    """Configuration for Production"""
    DEBUG = False
    TESTING = False
    SECURITY_PASSWORD_SALT = os.getenv('SALT')

app_config ={
    'development':DevelopementConfig,
    'testing':TestingConfig,
    'staging':StagingConfig,
    'production':ProductionConfig
}
