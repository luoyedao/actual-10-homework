class DevelopmentConfig():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI='mysql://wd:123456@192.168.1.251/test'

class ProductionConfig():
    SQLALCHEMY_DATABASE_URI='mysql://wd:123456@192.168.1.251/devops'

config = {
    'dev' : DevelopmentConfig,
    'pro' : ProductionConfig,
    'default' : DevelopmentConfig
}
