import json
import requests
from flask import current_app
from app.core import lexer,token_exprs

def parse(text):
    result =[]
    token_table= 'Sequence' + '(Token  , token type)\n'
    result.append(token_table)
    tokens = lexer(text, token_exprs)

    if not isinstance(tokens, list):
        error = 'The {} line: Syntax error(0) the\' {}\' token cannot be recognized'.format(tokens['line'], tokens['character'])
        print(error)
        return error
    for i,token in enumerate(tokens):
        token_table = '[{}] {}\n'.format(i,str(token))
        result.append(token_table)
        # token_table+
    print(token_table)
    return result
    # return json.loads(r.content.decode('utf-8-sig'))