from lexer import TokenType

class NumberNode:
    def __init__(self, token):
        self.token = token
        self.value = token.value
    
    def __repr__(self):
        return f"NumberNode({self.value})"

class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"BinOpNode({self.left}, {self.op}, {self.right})"
    
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[0]

    def advance(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos] 

    def parse(self):
        return self.expr()
    
    def expr(self):
        left = self.term()

        while self.current_token.type in (TokenType.PLUS,TokenType.MINUS):
            op = self.current_token
            self.advance()
            right = self.term()
            left = BinOpNode(left, op, right)

        return left
    
    def term(self):
        left = NumberNode(self.current_token)
        self.advance()

        while self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            op = self.current_token
            self.advance()
            right = NumberNode(self.current_token)
            self.advance()
            left = BinOpNode(left, op, right)

        return left