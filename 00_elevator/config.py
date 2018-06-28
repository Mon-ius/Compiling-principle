import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
                'fuckyouanywehre'
    LANGUAGES = ['en', 'es', 'zh_Hans_CN', 'zh_Hans', 'zh_CN','zh']
    BOOTSTRAP_SERVE_LOCAL = True
