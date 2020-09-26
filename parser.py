from ast import OneNode
from tokens import EOFToken
from symbol import SymTable


def parse(lexer):
    sym_table = SymTable()
    ast = OneNode(None, "# BEGIN PROGRAM\nnsv\n# END PROGRAM")

    next_token = lexer.lookahead()
    while next_token:
        if isinstance(next_token, EOFToken):
            break
        tree = next_token.parse_tree(lexer, sym_table)
        if tree:
            ast.add_child(tree)

        next_token = lexer.lookahead()

    return ast
