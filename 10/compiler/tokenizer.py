from collections import deque
from enum import Enum
from .tokens import Token, SYMBOLS

class Tokenizer:
    def __init__(self, filename):
        self.file = open(filename, "r")
        self.end_of_file = False
        self.is_block_comment = False

    def has_more_tokens(self):
        if self.tokens:
            return True
        else:
            while not self.end_of_file:
                while self.is_block_comment:
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

    def close(self):
        self.file.close()

    def _parse_line(self, line: str):
        tokens = deque()
        chars = ""
        for char in line:
            if char in SYMBOLS:
                # Check for comments and stop parsing current line
                if char == '*' and chars and chars[-1] == '/':
                    previous_chars = chars[:-1]
                    if previous_chars:
                        tokens.append(previous_chars)
                    self.is_block_comment = True
                    break
                if char == '/' and chars and chars[-1] == '/':
                    break
                elif chars:
                    tokens.append(chars)
                    chars = ""
                chars += char
            
            # Handle string literals
            elif char == '"':
                if chars and chars[0] == '"':
                    tokens.append(chars + char)
                    chars = ""
                else:
                    chars += char
            
            elif char.isspace():
                if chars and chars[0] == '"':
                    chars += char
                elif chars:
                    tokens.append(chars)
                    chars = ""
            else:
                chars += char
        return tokens

        def _find_comment_end(self):
            while self.is_block_comment:
                line = self.file.readline()
                if line == "":
                    self.end_of_file = True
                    break
                for i in range(1, len(line)):
                    if line[i] == "/" and line[i-1] == "*":
                        self.is_block_comment = False
                        break
