from new_pizza.errors import SyntaxError


class SymTable:
    def __init__(self, previous_scope=None):
        if previous_scope:
            self.symbols = {**previous_scope.symbols}
        else:
            self.symbols = {}

    def add_symbol(self, symbol, type=""):
        self.symbols[symbol.value] = symbol

    def check_symbol(self, symbol):
        if symbol.value not in self.symbols:
            raise SyntaxError(f"Symbol not defined: {symbol}")

    def new_scope(self):
        return SymTable(self)
