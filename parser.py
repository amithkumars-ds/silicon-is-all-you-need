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

class AssignNode:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"AssignNode{self.name}, {self.value}"

class VarNode:
    def __init__(self, token):
        self.name = token.value

    def __repr__(self):
        return f"VarNode({self.name})"

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
        if (self.current_token.type == TokenType.IDENTIFIER and
            self.pos + 1 < len(self.tokens) and 
            self.tokens[self.pos + 1].type == TokenType.ASSIGN):
            return self.assignment()
        return self.expr()
    
    def assignment(self):
        name = self.current_token.value
        self.advance() # skip identifier
        self.advance() # skip assignment = 
        value = self.expr()
        return AssignNode(name, value)
    
    def expr(self):
        left = self.term()

        while self.current_token.type in (TokenType.PLUS,TokenType.MINUS):
            op = self.current_token
            self.advance()
            right = self.term()
            left = BinOpNode(left, op, right)

        return left
    
    def factor(self):
        token = self.current_token
        if token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token)
        if token.type == TokenType.LPAREN:
            self.advance()
            result = self.expr()
            self.advance()
            return result 
        if token.type == TokenType.IDENTIFIER:
            self.advance()
            return VarNode(token)
    
    def term(self):
        left = self.factor()

        while self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            op = self.current_token
            self.advance()
            right = self.factor()
            self.advance()
            left = BinOpNode(left, op, right)

        return left