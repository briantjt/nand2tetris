from .tokenizer import Tokenizer
from .tokens import TokenType, KeywordType, SYMBOLS

indent = "  "

class CompilationEngine:
    def __init__(self, output_file, tokenizer):
        self.output_file = open(output_file, "w")
        self.tokenizer = tokenizer

    def close_file(self):
        self.output_file.close()
