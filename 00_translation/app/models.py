
class Post(object):
    def __init__(self,id,body='',language=''):
        self.id=id
        self.body=body
        self.language=language

    def __repr__(self):
        return '<Post {}>'.format(self.body)