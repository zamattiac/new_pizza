import re

from new_pizza.tokens import *
from new_pizza.errors import SyntaxError


class Lexer:
    symbols = {
        r"\|\>.*[\n\r]": CommentToken,
        r"comeinwereopen": StartToken,
        r"sorrywereclosed": EndToken,
        r"toppings": ToppingsToken,
        r"ooze": OozeToken,
        r"delivery": DeliveryToken,
        r"lemmegetta": LemmegettaToken,
        r"extra": ExtraToken,
        r"hold the": HoldTheToken,
        r";": EndStatementToken,
        r"[A-z0-9]+": LiteralToken,
        r"[\r\n]": NewlineToken,
        r"[ +\t\f]": UninterestingToken,
        r".+": Mismatch
    }

    r_str = "|".join([rf"(?P<{cls.__name__}>{kind})" for kind, cls in symbols.items()])
    regex = re.compile(r_str)

    def __init__(self, text):
        self.text = text
        self.feed = self.parse(text)

    def parse(self, text):
        tokens = []

        line_num = 1
        line_start = 0
        for token in self.regex.finditer(text):
            kind = token.lastgroup
            value = token.group()

            row = line_num
            col = token.start() - line_start

            token_class = eval(kind)

            if token_class == NewlineToken:
                line_num += 1
                line_start = token.end()

            if not issubclass(token_class, UninterestingToken):
                tokens.append(token_class(value, row, col))

        tokens.append(EOFToken("", line_num, 0))
        return tokens

    def lookahead(self):
        if self.feed:
            return self.feed[0]
        return None

    def pop(self):
        if self.feed:
            return self.feed.pop(0)
        raise SyntaxError("EOF Reached")

    def __iter__(self):
        return self

    def __next__(self):
        if self.feed:
            return self.pop()
        raise StopIteration

    def __str__(self):
        return ",".join([str(token) for token in self.feed])
