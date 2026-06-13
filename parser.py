from lexer import TokenType

class CallNode:
    def __init__(self, name, args):
        self.name = name # print
        self.args = args # list of AST nodes inside the ()

    def __repr__(self):
        return f"CallNode({self.name}, {self.args})"   
    
class NumberNode:
    def __init__(self, token):
        self.token = token
        self.value = token.value
    
    def __repr__(self):
        return f"NumberNode({self.value})"
    
class IfNode:
    def __init__(self, condition, true_expr, false_expr=None):
        self.condition = condition
        self.true_expr = true_expr
        self.false_expr = false_expr

    def __repr__(self):
        return f'IfNode({self.condition}, {self.true_expr}, {self.false_expr})'
    
class CompareNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f'CompareNode({self.left}, {self.op}, {self.right})'
    
class NotNode:
    def __init__(self, node):
        self.node = node

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
        if self.current_token.type == TokenType.IF:
            return self.if_expr()
        
        if (self.current_token.type == TokenType.IDENTIFIER and
            self.pos+1 < len(self.tokens) and
            self.tokens[self.pos+1].type == TokenType.ASSIGN):
            return self.assignment()
        
        return self.comparison()
    
    def assignment(self):
        name = self.current_token.value
        self.advance() # skip identifier
        self.advance() # skip assignment = 
        value = self.comparison()
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
        if token.type == TokenType.NOT:
            self.advance()
            return NotNode(self.factor())
        if token.type == TokenType.IDENTIFIER:
            self.advance()
            args = []
            if self.current_token.type == TokenType.LPAREN:
                self.advance()
                while self.current_token.type != TokenType.RPAREN:
                    args.append(self.expr())
                    if self.current_token.type == TokenType.COMMA:
                        self.advance()
                self.advance()
                return CallNode(token.value, args)
            else:
                return VarNode(token)

    
    def term(self):
        left = self.factor()

        while self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            op = self.current_token
            self.advance()
            right = self.factor()
            left = BinOpNode(left, op, right)

        return left
    
    def if_expr(self):
        self.advance()

        condition = self.comparison()
        true_expr = self.comparison()

        false_expr = None
        if self.current_token.type == TokenType.ELSE:
            self.advance()
            false_expr = self.comparison()

        return IfNode(condition, true_expr, false_expr)
    

    def comparison(self):
        left = self.expr()

        if self.current_token.type in (
            TokenType.GREATER_THAN,
            TokenType.GREATER_THAN_EQUAL,
            TokenType.LESSER_THAN,
            TokenType.LESSER_THAN_EQUAL,
            TokenType.COMPARISON_EQUALS,
            TokenType.COMPARISON_NOT_EQUALS
        ):
            op = self.current_token
            self.advance()
            right = self.expr()
            return CompareNode(left, op, right)
        
        return left
    
    