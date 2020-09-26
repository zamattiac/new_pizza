from lexer import Lexer
from parser import parse

text = """
toppings cheese 3
hold the cheese

comeinwereopen 
toppings cheese 10

|> hello world!
ooze hello hi;

|> set values
lemmegetta cheese 4
extra cheese
lemmegetta cheese 5

|> print the first value
hold the cheese
ooze delivery cheese;

|> end main program
sorrywereclosed
"""

lexer = Lexer(text)

ast = parse(lexer)

print(ast.crawl_tree())
