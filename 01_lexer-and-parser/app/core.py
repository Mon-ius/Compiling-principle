import re


ENTER = 'Enter(Change Line)'
KEYWORD = 'Keyword'
INT = 'Int'
DOUBLE = 'Double'
VAR = 'Variable'
COMMENT = 'Comment'
SPACE = 'Space'
STRING = 'String'

token_exprs = [
    (r'[\n]+', ENTER),
    (r'[ \t]+', SPACE),
    (r'#[^\n]*', None),
    (r'\d\.\d', DOUBLE),
    # (r'[//]*',COMMENT),
    (r'\:', KEYWORD),
    (r'\=', KEYWORD),
    (r'\(', KEYWORD),
    (r'\)', KEYWORD),
    (r';', KEYWORD),
    (r'\+', KEYWORD),
    (r'-', KEYWORD),
    (r'\*', KEYWORD),
    (r'/', KEYWORD),
    (r'<=', KEYWORD),
    (r'<', KEYWORD),
    (r'>=', KEYWORD),
    (r'>', KEYWORD),
    (r'!=', KEYWORD),
    (r'=', KEYWORD),
    (r'and', KEYWORD),
    (r'or', KEYWORD),
    (r'not', KEYWORD),
    (r'if', KEYWORD),
    (r'then', KEYWORD),
    (r'else', KEYWORD),
    (r'while',KEYWORD),
    (r'do', KEYWORD),
    (r'continue', KEYWORD),
    (r'end', KEYWORD),
    # (r'-[0-9]+', NINT)
    (r'[0-9]+', INT),
    #(r'\/\*'),
    (r'(\'[ A-Z a-z 0-9 ]+\')|(\"[ A-Z a-z 0-9 ]+\")$',STRING),
    (r'[A-Za-z][A-Za-z0-9_]*', VAR),
]

def lexer(characters, token_exprs):
    pos = 0
    tokens = []
    line_number = 1
    while pos < len(characters):
        match = None
        for token_expr in token_exprs:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(characters, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    if tag == 'Enter(Change Line)':
                        line_number = line_number + 1
                    tokens.append(token)
                break
        if not match:
            dict = {'line':line_number,
                    'character':characters[pos]}
            return dict
        else:
            pos = match.end(0)
    return tokens