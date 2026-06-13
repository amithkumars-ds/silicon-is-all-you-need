from lexer import TokenType
from parser import BinOpNode, NumberNode, VarNode, AssignNode, CallNode, IfNode, CompareNode, NotNode

class Evaluator:
    def __init__(self):
        self.symbol_table = {}

    def visit(self, node):
        if isinstance(node, CallNode):
            if node.name == 'printk':
                args = [self.visit(arg) for arg in node.args]
                print(*args)
                return None
        if isinstance(node, NumberNode):
            return node.value
        if isinstance(node, VarNode):
            return self.symbol_table[node.name]
        if isinstance(node, AssignNode):
            value = self.visit(node.value)
            self.symbol_table[node.name] = value
            return value 
        if isinstance(node, IfNode):
            condition = self.visit(node.condition)
            if condition:
                return self.visit(node.true_expr)
            if node.false_expr is not None:
                return self.visit(node.false_expr)
            return None
        if isinstance(node, NotNode):
            return not self.visit(node.node)
        if isinstance(self, CompareNode):
            left = self.visit(node.left)
            right = self.visit(node.right)
            if node.op.type == TokenType.GREATER_THAN:
                return left > right
            if node.op.type == TokenType.GREATER_THAN_EQUAL:
                return left >= right
            if node.op.type == TokenType.LESSER_THAN:
                return left < right
            if node.op.type == TokenType.LESSER_THAN_EQUAL:
                return left <= right
            if node.op.type == TokenType.COMPARISON_EQUALS:
                return left == right
            if node.op.type == TokenType.COMPARISON_NOT_EQUALS:
                return left != right
        if isinstance(node, CompareNode):
            left = self.visit(node.left)
            right = self.visit(node.right)

            if node.op.type == TokenType.GREATER_THAN:
                return left > right
            if node.op.type == TokenType.GREATER_THAN_EQUAL:
                return left >= right
            if node.op.type == TokenType.LESSER_THAN:
                return left < right
            if node.op.type == TokenType.LESSER_THAN_EQUAL:
                return left <= right
            if node.op.type == TokenType.COMPARISON_EQUALS:
                return left == right
            if node.op.type == TokenType.COMPARISON_NOT_EQUALS:
                return left != right
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

