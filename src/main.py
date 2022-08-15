from load import loadtext
from lexer import lexer
from parser import parser
src = loadtext()
tokens = lexer(src)
parser(tokens)
print(tokens)
