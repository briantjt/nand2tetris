from collections import deque
from .tokens import Token, SYMBOLS

class Tokenizer:
    def __init__(self, filename):
        self.file = open(filename, "r")
        self.tokens = deque()
        self.end_of_file = False
        self.is_block_comment = False

    def has_more_tokens(self):
        if self.tokens:
            return True
        else:
            while not self.end_of_file:
                while self.is_block_comment and not self.end_of_file:
                    self._find_comment_end()
                line = self.file.readline()
                if not line:
                    self.end_of_file = True
                    return False
                else:
                    tokens = self._parse_line(line)

                    if not tokens:
                        continue
                    self.tokens = tokens
                    return True
            return False

    def pop_next_token(self):
        return Token(self.tokens.popleft())

    def close_file(self):
        self.file.close()

    def _parse_line(self, line: str):
        tokens = deque()
        chars = ""
        potential_comment_start = False
        potential_comment_end = False
        for char in line:
            if self.is_block_comment:
                if char == "*":
                    potential_comment_end = True
                elif char == "/" and potential_comment_end:
                    self.is_block_comment = False
                    chars = ""
                else:
                    potential_comment_end = False

            elif char in SYMBOLS:
                # Check for comments and stop parsing current line
                if char == '*' and potential_comment_start:
                    tokens.pop()
                    self.is_block_comment = True
                elif char == '/' and potential_comment_start:
                    tokens.pop()
                    return tokens
                elif char == '/':
                    tokens.append(char)
                    potential_comment_start = True
                else:
                    if chars:
                        tokens.append(chars)
                        chars = ""
                    potential_comment_start = False
                    tokens.append(char)
                    
            
            # Handle string literals
            elif char == '"':
                if chars and chars[0] == '"':
                    tokens.append(chars + char)
                    chars = ""
                else:
                    if chars:
                        tokens.append(chars)
                    chars = char
            
            elif char.isspace():
                if chars and chars[0] == '"':
                    chars += char
                elif chars:
                    tokens.append(chars)
                    chars = ""

            else:
                chars += char
        if chars:
            tokens.append(chars)
        return tokens

    def _find_comment_end(self):
        while self.is_block_comment:
            line = self.file.readline()
            if not line:
                self.end_of_file = True
                break
            for i in range(1, len(line)):
                if line[i] == "/" and line[i-1] == "*":
                    self.is_block_comment = False
                    break
