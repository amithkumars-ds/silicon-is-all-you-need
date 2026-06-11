import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lexer import Lexer, TokenType

def tokenize(text):
    return Lexer(text).tokenize()

def types(text):
    return [t.type for t in tokenize(text)]

def values(text):
    return [t.value for t in tokenize(text)]

# --- Numbers and basic arithmetic ---

def test_single_number():
    assert types('42') == [TokenType.NUMBER, TokenType.EOF]

def test_addition():
    assert types('1 + 2') == [TokenType.NUMBER, TokenType.PLUS, TokenType.NUMBER, TokenType.EOF]

def test_subtraction():
    assert types('5 - 3') == [TokenType.NUMBER, TokenType.MINUS, TokenType.NUMBER, TokenType.EOF]

def test_multiply():
    assert types('4 * 2') == [TokenType.NUMBER, TokenType.MULTIPLY, TokenType.NUMBER, TokenType.EOF]

def test_divide():
    assert types('8 / 2') == [TokenType.NUMBER, TokenType.DIVIDE, TokenType.NUMBER, TokenType.EOF]

# --- Identifiers and keywords ---

def test_identifier():
    assert types('x') == [TokenType.IDENTIFIER, TokenType.EOF]

def test_keyword_if():
    assert types('if') == [TokenType.IF, TokenType.EOF]

def test_keyword_else():
    assert types('else') == [TokenType.ELSE, TokenType.EOF]

# --- Assignment ---

def test_assign():
    assert types('x = 5') == [TokenType.IDENTIFIER, TokenType.ASSIGN, TokenType.NUMBER, TokenType.EOF]

# --- Comparison operators ---

def test_equals():
    assert types('x == 5') == [TokenType.IDENTIFIER, TokenType.COMPARISON_EQUALS, TokenType.NUMBER, TokenType.EOF]

def test_not_equals():
    assert types('x != 5') == [TokenType.IDENTIFIER, TokenType.COMPARISON_NOT_EQUALS, TokenType.NUMBER, TokenType.EOF]

def test_greater_than():
    assert types('x > 5') == [TokenType.IDENTIFIER, TokenType.GREATER_THAN, TokenType.NUMBER, TokenType.EOF]

def test_lesser_than():
    assert types('x < 5') == [TokenType.IDENTIFIER, TokenType.LESSER_THAN, TokenType.NUMBER, TokenType.EOF]

def test_greater_than_equal():
    assert types('x >= 5') == [TokenType.IDENTIFIER, TokenType.GREATER_THAN_EQUAL, TokenType.NUMBER, TokenType.EOF]

def test_lesser_than_equal():
    assert types('x <= 5') == [TokenType.IDENTIFIER, TokenType.LESSER_THAN_EQUAL, TokenType.NUMBER, TokenType.EOF]

# --- Parentheses and comma ---

def test_parens():
    assert types('(x + 5)') == [TokenType.LPAREN, TokenType.IDENTIFIER, TokenType.PLUS, TokenType.NUMBER, TokenType.RPAREN, TokenType.EOF]

def test_comma():
    assert types('x, y') == [TokenType.IDENTIFIER, TokenType.COMMA, TokenType.IDENTIFIER, TokenType.EOF]

# --- Unknown character raises exception ---

def test_unknown_character():
    with pytest.raises(Exception, match="Unkown character"):
        Lexer('@x').tokenize()