from new_pizza.ast import OneNode
from new_pizza.errors import ParseError, SyntaxError


class Token:
    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col

    def __str__(self):
        return f"<{self.__class__.__name__} {self.row}:{self.col}>"

    def parse_tree(self, tokens_list, sym_table):
        raise NotImplementedError

    def parse_children(self, tokens_list, sym_table, end_type=None):
        next_token = tokens_list.lookahead()

        while not isinstance(next_token, end_type):
            if isinstance(next_token, EOFToken):
                raise ParseError(f"EOF Reached for {self.__class__.__name__}")

            child_tree = next_token.parse_tree(tokens_list, sym_table)
            if child_tree:
                yield child_tree

            next_token = tokens_list.lookahead()

    def become_identifier(self):
        if isinstance(self, LiteralToken):
            self.__class__ = IdentifierToken
        else:
            raise SyntaxError(f"Expected a literal for {self.__class__.__name__}")


class StartToken(Token):
    def parse_tree(self, tokens_list, sym_table):
        start_token = tokens_list.pop()

        t = OneNode(start_token, "# BEGIN MAIN\nnsv\n# END MAIN")

        new_table = sym_table.new_scope()
        for child in self.parse_children(tokens_list, new_table, EndToken):
            t.add_child(child)

        return t


class EndToken(Token):
    def parse_tree(self, tokens_list, sym_table):
        next_token = tokens_list.pop()


class ToppingsToken(Token):
    def parse_tree(self, tokens_list, sym_table):
        token = tokens_list.pop()

        t = OneNode(token, "first=[None]*second\nfirst_index=0")
        array = tokens_list.pop()
        size = tokens_list.pop()
        t.add_child(array)
        t.add_child(size)

        array.become_identifier()
        sym_table.add_symbol(array)

        return t


class OozeToken(Token):
    def parse_tree(self, tokens_list, sym_table):
        ooze_token = tokens_list.pop()
        t = OneNode(ooze_token, "print(f'csv') # OOZE")

        for child in self.parse_children(tokens_list, sym_table, EndStatementToken):
            t.add_child(child)

        return t


class DeliveryToken(Token):
    def parse_tree(self, tokens_list, sym_table):
        delivery_token = tokens_list.pop()

        t = OneNode(delivery_token, "first[first_index] # ACCESS MEMORY")
        array = tokens_list.pop()
        array.become_identifier()

        sym_table.check_symbol(array)

        t.add_child(array)

        return t


class LemmegettaToken(Token):
    def parse_tree(self, tokens_list, sym_table):
        token = tokens_list.pop()

        t = OneNode(token, "first[first_index] = second # SET MEMORY")
        array = tokens_list.pop()
        array.become_identifier()

        sym_table.check_symbol(array)

        value = tokens_list.pop()
        t.add_child(array)
        t.add_child(value)

        return t


class HoldTheToken(Token):
    def parse_tree(self, tokens_list, sym_table):
        token = tokens_list.pop()

        t = OneNode(token, "first_index=0 # RESET ARRAY")
        array = tokens_list.pop()
        array.become_identifier()

        sym_table.check_symbol(array)

        t.add_child(array)

        return t


class ExtraToken(Token):
    def parse_tree(self, tokens_list, sym_table):
        token = tokens_list.pop()

        t = OneNode(token, "first_index+=1")
        array = tokens_list.pop()
        array.become_identifier()

        sym_table.check_symbol(array)

        t.add_child(array)

        return t


class EndStatementToken(Token):
    def parse_tree(self, tokens_list, sym_table):
        tokens_list.pop()


class IdentifierToken(Token):
    def parse_tree(self, tokens_list, sym_table):
        return tokens_list.pop()

    def __str__(self):
        return f"<{self.__class__.__name__} {self.value} {self.row}:{self.col}>"


class LiteralToken(Token):
    def parse_tree(self, tokens_list, sym_table):
        return tokens_list.pop()

    def __str__(self):
        return f"<{self.__class__.__name__} {self.value} {self.row}:{self.col}>"


class UninterestingToken(Token):
    def parse_tree(self, tokens_list, sym_table):
        pass


class CommentToken(UninterestingToken):
    def parse_tree(self, tokens_list, sym_table):
        next_token = tokens_list.pop()


class NewlineToken(Token):
    def parse_tree(self, tokens_list, sym_table):
        next_token = tokens_list.pop()


class EOFToken(Token):
    def parse_tree(self, tokens_list, sym_table):
        tokens_list.pop()


class Mismatch(Token):
    def __init__(self, value, row, col):
        super().__init__(value, row, col)
        raise Exception(f"BAD VALUE {value}")

    def parse_tree(self, tokens_list, sym_table):
        pass
