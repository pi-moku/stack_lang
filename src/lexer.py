import re
def lexer(src):
    tokens = re.split('\/\/.*$|(".*"|push)|\n', src)
    if 'pendp' in tokens:
        for t in range(tokens.count('pendp')):
            tokens.remove('pendp')
    if None in tokens:
        for r in range(tokens.count(None)):
            tokens.remove(None)
    if '' in tokens:
        for g in range(tokens.count('')):
            tokens.remove('')
    tokens.append('pendp')
    return tokens
