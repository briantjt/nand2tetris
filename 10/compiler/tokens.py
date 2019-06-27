from enum import Enum


class TokenType(Enum):
    KEYWORD = 1
    SYMBOL = 2
    IDENTIFIER = 3
    INT_CONST = 4
    STRING_CONST = 5


class KeywordType(Enum):
    CLASS = 1
    METHOD = 2
    FUNCTION = 3
    CONSTRUCTOR = 4
    INT = 5
    BOOLEAN = 6
    CHAR = 7
    VOID = 8
    VAR = 9
    STATIC = 10
    FIELD = 11
    LET = 12
    DO = 13
    IF = 14
    ELSE = 15
    WHILE = 16
    RETURN = 17
    TRUE = 18
    FALSE = 19
    NULL = 20
    THIS = 21


SYMBOLS = {
    '{',
    '}',
    '(',
    ')',
    '[',
    ']',
    '.',
    ',',
    ';',
    '+',
    '-',
    '*',
    '/',
    '&',
    '|',
    '<',
    '>',
    '=',
    '~'
}

TOKEN_TAGS = {
    TokenType.IDENTIFIER: 'identifier',
    TokenType.INT_CONST: 'integerConstant',
    TokenType.KEYWORD: 'keyword',
    TokenType.STRING_CONST: 'stringConstant',
    TokenType.SYMBOL: 'symbol'
}

KEYWORDS = set()

for keyword in KeywordType:
    KEYWORDS.add(keyword.name.lower())


class Token:
    def __init__(self, value: str):
        self.value = value
        self.token_type = self._get_token_type()

    def _get_token_type(self):
        if self.value in SYMBOLS:
            return TokenType.SYMBOL
        elif self.value in KEYWORDS:
            return TokenType.KEYWORD
        elif self.value[0].isnumeric():
            return TokenType.INT_CONST
        elif self.value[0] == '"':
            self.value = self.value[1:-1]
            return TokenType.STRING_CONST
        else:
            return TokenType.IDENTIFIER
