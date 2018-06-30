import json
import requests
from flask import current_app
from app.core import ExpressionEvaluator

def parse(text):

    token_table= ['Result:']
    print(text)

    e = ExpressionEvaluator()
    try:
        result=e.parse(str(text))
    except SyntaxError:
        error = 'SyntaxError!!! Expected NUMBER or LPAREN'
        print(error)
        return [error,'Failed.']

    print(result)
    token_table.append(result)
    token_table.append('Successful.')
    return token_table

