#!/usr/bin/env python

from sqlalchemy import Column, Integer, String
from werkzeug import generate_password_hash, check_password_hash
from database import Base

class User(Base):
    __tablename__ = 'users'
    id       = Column(Integer, primary_key=True)
    # name     = Column(String(50), unique=True)
    # email    = Column(String(120), unique=True)
    username = Column(String(50), unique=True)
    pw_hash  = Column(String(80))

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
        #self.email = email

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

    def __repr__(self):
        return '<User %r>' % (self.username)
