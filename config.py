#!/usr/bin/env python
class Config(object):
    DEBUG        = False
    TESTING      = False
    DATABASE_URI = 'sqlite://:memory:'

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG        = True
    SECRET_KEY   = '2b020728f54c912f4635135459b17d8a54e2dabc'

class TestinConfig(Config):
    TESTING = True

