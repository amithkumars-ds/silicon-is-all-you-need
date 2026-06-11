class TokenType:
    NUMBER = 'NUMBER'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    MULTIPLY = 'MULTIPLY'
    DIVIDE = 'DIVIDE'
    ASSIGN = 'ASSIGN'
    IDENTIFIER = 'IDENTIFIER'
    EOF = 'EOF'
    LPAREN = 'LPAREN'
    RPAREN = 'RPAREN'
    COMMA = 'COMMA'
    IF = 'IF'
    ELSE = 'ELSE'
    GREATER_THAN = 'GREATER_THAN'
    GREATER_THAN_EQUAL = 'GREATER_THAN_EQUAL'
    LESSER_THAN = 'LESSER_THAN'
    LESSER_THAN_EQUAL = 'LESSER_THAN_EQUAL'
    COMPARISON_EQUALS = 'COMPARISON_EQUALS'
    COMPARISON_NOT_EQUALS = 'COMPARISON_NOT_EQUALS'
    NOT = 'NOT'

class constants:
    KEYWORDS = {
                'if': TokenType.IF,
                'else': TokenType.ELSE
                }

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"
    
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[0]

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def peek(self):
        peek_pos = self.pos + 1
        if peek_pos < len(self.text):
            return self.text[peek_pos]
        return None
        
    def skip_white_space(self,):
        while self.current_char is not None and self.current_char == ' ':
            self.advance()
    
    def number(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return Token(TokenType.NUMBER, int(result))
    
    def identifier(self):
        result = ''
        while self.current_char is not None and self.current_char.isalnum():
            result += self.current_char
            self.advance()
        token_type = constants.KEYWORDS.get(result, TokenType.IDENTIFIER)
        return Token(token_type, result)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char == ' ':
                self.skip_white_space()
                continue
            if self.current_char.isdigit():
                return self.number()
            if self.current_char == '+':
                self.advance()
                return Token(TokenType.PLUS, '+')
            if self.current_char == '-':
                self.advance()
                return Token(TokenType.MINUS, '-')
            if self.current_char == '*':
                self.advance()
                return Token(TokenType.MULTIPLY, '*')
            if self.current_char == '/':
                self.advance()
                return Token(TokenType.DIVIDE, '/')
            if self.current_char == '=':
                if self.peek() == '=':
                    self.advance()
                    self.advance()
                    return Token(TokenType.COMPARISON_EQUALS, '==')
                self.advance()
                return Token(TokenType.ASSIGN, '=')
            if self.current_char == '!':
                if self.peek() == '=':
                    self.advance()
                    self.advance()
                    return Token(TokenType.COMPARISON_NOT_EQUALS, '!=')
                return Token(TokenType.NOT, '!')
            if self.current_char == '(':
                self.advance()
                return Token(TokenType.LPAREN, '(')
            if self.current_char == ')':
                self.advance()
                return Token(TokenType.RPAREN, ')')
            if self.current_char.isalpha():
                return self.identifier()
            if self.current_char == '>':
                if self.peek() == '=':
                    self.advance()
                    self.advance()
                    return Token(TokenType.GREATER_THAN_EQUAL, '>=')
                self.advance()
                return Token(TokenType.GREATER_THAN, '>')
            if self.current_char == '<':
                if self.peek() == '=':
                    self.advance()
                    self.advance()
                    return Token(TokenType.LESSER_THAN_EQUAL, '<=')
                self.advance()
                return Token(TokenType.LESSER_THAN, '<')
            if self.current_char == ',':
                self.advance()
                return Token(TokenType.COMMA, ',')
            raise Exception(f"Unkown character: {self.current_char}")
        return Token(TokenType.EOF, None)
    
    def tokenize(self):
        tokens = []
        while self.current_char is not None:
            tokens.append(self.get_next_token())
        tokens.append(Token(TokenType.EOF, None))
        
        return tokens
    


if __name__ == '__main__':
    tests = [
        'x == 5',
        'x != 5',
        'x >= 5',
        'x <= 5',
        'if x > 5',
        'else',
    ]
    for test in tests:
        lexer = Lexer(test)
        print(lexer.tokenize())