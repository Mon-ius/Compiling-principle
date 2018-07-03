import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
                'fuckyousadsade'
    LANGUAGES = ['en', 'es', 'zh_Hans_CN', 'zh_Hans', 'zh_CN','zh']
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY') or '1e279379821349fd9eec958404703fe9'
    BOOTSTRAP_SERVE_LOCAL = True