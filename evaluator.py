from lexer import TokenType
from parser import BinOpNode, NumberNode, VarNode, AssignNode

class Evaluator:
    def __init__(self):
        self.symbol_table = {}

    def visit(self, node):
        if isinstance(node, NumberNode):
            return node.value
        if isinstance(node, VarNode):
            return self.symbol_table[node.name]
        if isinstance(node, AssignNode):
            value = self.visit(node.value)
            self.symbol_table[node.name] = value
            return value 
        if isinstance(node, BinOpNode):
            left = self.visit(node.left)
            right = self.visit(node.right)
            if node.op.type == TokenType.PLUS:
                return left + right
            if node.op.type == TokenType.MINUS:
                return left - right
            if node.op.type == TokenType.MULTIPLY:
                return left * right
            if node.op.type == TokenType.DIVIDE:
                return left // right

if __name__ == '__main__':
    from lexer import Lexer
    from parser import Parser

    evaluator = Evaluator()

    for line in ['x = 10', 'y = 5', 'x + y']:
        lexer = Lexer(line)
        tokens = lexer.tokenize()
        ast = Parser(tokens).parse()
        result = evaluator.visit(ast)
        print(result)