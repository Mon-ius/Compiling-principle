import json
import requests
from flask import current_app
from app.core import lexer

# '(t1+p)*(2+2)'
def parse(text):
    result =[]

    tokens = lexer(text)
    for  i,res in tokens.items():
        for r in res:
            result.append(r)
    return result
    # return json.loads(r.content.decode('utf-8-sig'))