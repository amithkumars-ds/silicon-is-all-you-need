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
        left = NumberNode(self.current_token)
        self.advance()

        op = self.current_token
        self.advance()

        right = NumberNode(self.current_token)
        self.advance()

        return BinOpNode(left, op, right)
    


from lexer import Lexer
lexer = Lexer('10+5')
tokens = lexer.tokenize()
print(tokens)

parser  = Parser(tokens)
ast = parser.parse()
print(ast)