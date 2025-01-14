import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "W#jQ0fwVhH^'Fyqr+MZ^axtF)LKbWBwFr0ect2GS.9iZ!M~>#9<4]exR!t$6E6"
    JWT_COOKIE_SECURE = False
    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_COOKIE_CSRF_PROTECT=False
    MAIL_SERVER='email-smtp.eu-central-1.amazonaws.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'AKIAWKJEZSOKD57VRAPE'
    MAIL_PASSWORD = 'BM/hxGfDHxke8L0DhERHnMSmNhOYe8VNvXsRLWiQBdqT'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = True
