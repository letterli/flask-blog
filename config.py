# _*_ coding: utf-8 _*_

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')              # 实现CSRF保护  Flask-WTF使用密钥生成加密令牌，再用加密令牌验证表单数据真伪
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True      # 每次请求结束后都会自动提交数据库变动
    FLASK_ARTICLES_PER_PAGE = 10
    # Flask-Mail 相关的配置
    MAIL_USE_TLS = True
    MAIL_USE_SSL = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 587
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flask]'
    FLASKY_MAIL_SENDER = 'Flask Admin <infzmserver@163.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentCofig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123@127.0.0.1/flask_blog'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@hostname/database'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@hostname/database'

config = {
    'development': DevelopmentCofig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentCofig
}


