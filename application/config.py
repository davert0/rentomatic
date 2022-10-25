import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """Base configuration"""


class ProductionConfig(Config):
    """Prod config"""


class DevConfig(Config):
    """Dev config"""


class TestingConfig(Config):
    """Testing config"""

    TESTING = True


