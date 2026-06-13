import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lexer import Lexer
from parser import Parser
from evaluator import Evaluator


def run_line(evaluator, text):
    tokens = Lexer(text).tokenize()
    ast = Parser(tokens).parse()
    return evaluator.visit(ast)


def test_assignment():
    evaluator = Evaluator()

    result = run_line(evaluator, 'x = 10')

    assert result == 10
    assert evaluator.symbol_table['x'] == 10


def test_variable_lookup():
    evaluator = Evaluator()

    run_line(evaluator, 'x = 10')
    result = run_line(evaluator, 'x')

    assert result == 10


def test_addition_with_variables():
    evaluator = Evaluator()

    run_line(evaluator, 'x = 10')
    run_line(evaluator, 'y = 5')

    result = run_line(evaluator, 'x + y')

    assert result == 15


def test_greater_than_true():
    evaluator = Evaluator()

    run_line(evaluator, 'x = 10')

    result = run_line(evaluator, 'x > 5')

    assert result is True


def test_greater_than_false():
    evaluator = Evaluator()

    run_line(evaluator, 'x = 10')

    result = run_line(evaluator, 'x > 20')

    assert result is False


def test_equals_true():
    evaluator = Evaluator()

    run_line(evaluator, 'x = 10')

    result = run_line(evaluator, 'x == 10')

    assert result is True


def test_not_equals_true():
    evaluator = Evaluator()

    run_line(evaluator, 'x = 10')

    result = run_line(evaluator, 'x != 5')

    assert result is True


def test_if_true_branch():
    evaluator = Evaluator()

    run_line(evaluator, 'x = 10')
    run_line(evaluator, 'y = 5')

    result = run_line(evaluator, 'if x > y x else y')

    assert result == 10


def test_if_false_branch():
    evaluator = Evaluator()

    run_line(evaluator, 'x = 10')
    run_line(evaluator, 'y = 5')

    result = run_line(evaluator, 'if x < y x else y')

    assert result == 5


def test_if_without_else_true():
    evaluator = Evaluator()

    run_line(evaluator, 'x = 10')

    result = run_line(evaluator, 'if x == 10 x')

    assert result == 10


def test_if_without_else_false():
    evaluator = Evaluator()

    run_line(evaluator, 'x = 10')

    result = run_line(evaluator, 'if x == 5 x')

    assert result is None


def test_if_with_expression_branch():
    evaluator = Evaluator()

    run_line(evaluator, 'x = 10')
    run_line(evaluator, 'y = 5')

    result = run_line(evaluator, 'if x > y x + y else y')

    assert result == 15


def test_printk_single_value(capsys):
    evaluator = Evaluator()

    run_line(evaluator, 'x = 10')
    run_line(evaluator, 'printk(x)')

    captured = capsys.readouterr()

    assert captured.out.strip() == '10'


def test_if_true_with_printk(capsys):
    evaluator = Evaluator()

    run_line(evaluator, 'x = 10')
    run_line(evaluator, 'y = 5')

    run_line(evaluator, 'if x > y printk(x) else printk(y)')

    captured = capsys.readouterr()

    assert captured.out.strip() == '10'


def test_if_false_with_printk(capsys):
    evaluator = Evaluator()

    run_line(evaluator, 'x = 10')
    run_line(evaluator, 'y = 5')

    run_line(evaluator, 'if x < y printk(x) else printk(y)')

    captured = capsys.readouterr()

    assert captured.out.strip() == '5'