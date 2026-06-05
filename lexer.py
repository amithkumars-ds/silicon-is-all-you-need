class TokenType:
    NUMBER = 'NUMBER'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    MULTIPLY = 'MULTIPLY'
    ASSIGN = 'ASSIGN'
    IDENTIFIER = 'IDENTIFIER'
    EOF = 'EOF'

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
        
    def skip_white_space(self,):
        while self.current_char is not None and self.current_char == ' ':
            self.advance()
    
    def number(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return Token(TokenType.NUMBER, int(result))
    
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
            if self.current_char == '=':
                self.advance()
                return Token(TokenType.ASSIGN, '=')
        return Token(TokenType.EOF, None)
    
    def tokenize(self):
        tokens = []
        while self.current_char is not None:
            tokens.append(self.get_next_token())
        tokens.append(Token(TokenType.EOF, None))
        
        return tokens
        
# lexer = Lexer('10+5')
# print(lexer.tokenize())