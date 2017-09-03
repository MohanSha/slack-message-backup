import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "2358h2wfnij98hui352noiwfjhuon532j"#os.environ.get("SECRET_KEY")
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = "[Holberton School Slack Backup]"
    FLASKY_MAIL_SENDER = "Admin <holbertonslackbackup@gmail.com>"
    FLASKY_ADMIN = os.environ.get("FLASKY_ADMIN") or "Steven G."
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    @staticmethod
    def init_app (app):
        pass

class DevelopmentConfig(Config):
        DEBUG = True
        SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data-dev.sqlite")

class TestingConfig(Config):
        TESTING = True
        SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data-test.sqlite")

class ProductionConfig(Config):
        TESTING = True
        SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data-prod.sqlite")

config = {
        "development" : DevelopmentConfig,
        "testing": TestingConfig,
        "production": ProductionConfig,
        "default": DevelopmentConfig
    }
