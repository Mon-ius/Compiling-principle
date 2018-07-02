import json
import requests
from flask import current_app
from app.core import lexer

# text = ['E->E+T',
#     'E->T',
#     'T->F',
#     'T->T*F',
#     'F->P',
#     'F->P^F',
#     'P->(E)',
#     'P->i']
# E->E+T
# E->T
# T->F
# T->T*F
# F->P
# F->P^F
# P->(E)
# P->i
def parse(text):
    result =[]

    tokens = lexer(text)
    for i in tokens:
        result.append(i)
    return result
    # return json.loads(r.content.decode('utf-8-sig'))