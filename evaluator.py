from lexer import TokenType
from parser import BinOpNode, NumberNode

class Evaluator:
    def visit(self, node):
        if isinstance(node, NumberNode):
            return node.value
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

    lexer = Lexer('(2 + 3) * (4 + 1)')
    tokens = lexer.tokenize()
    ast = Parser(tokens).parse()

    evaluator = Evaluator()
    result = evaluator.visit(ast)
    print(result)