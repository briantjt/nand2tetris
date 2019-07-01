"""Compiles Jackfiles into bytecode"""
from compiler.tokenizer import Tokenizer
from compiler.tokens import TokenType, TOKEN_TAGS, Token
import html

INDENT = "  "

CLASS_VAR_DECS = {"static", "field"}
SUBROUTINE_DECS = {"constructor", "function", "method"}
TYPE_DECS = {"int", "char", "boolean"}
STATEMENTS = {"let", "if", "while", "do", "return"}
OPERATORS = {"+", "-", "*", "/", "&", "|", "<", ">", "="}
KEYWORD_CONST = {"true", "false", "null", "this"}
UNARY_OPS = {"~", "-"}


class CompilationEngine:
    """Controls all the code generation """

    def __init__(self, output_file, tokenizer: Tokenizer):
        self.output_file = open(output_file, "w")
        self.tokenizer = tokenizer
        self.indent_level = 0

    def close_file(self):
        """ Closes the input file """
        self.output_file.close()

    def compile_class(self):
        """Entrypoint method that compiles the entire file/class"""

        # Class declaration
        class_keyword = self._next_token(values=["class"])
        self._write("<class>\n")
        self._write_token(class_keyword)
        class_id = self._next_token(token_types=[TokenType.IDENTIFIER])
        self._write_token(class_id)
        opening_bracket = self._next_token(values=["{"])
        self._write_token(opening_bracket)

        # Compile Var/Subroutine Declarations
        while self.tokenizer.has_more_tokens():
            class_body = self._next_token(
                values=["static", "field", "constructor", "function", "method", "}"])
            if class_body.value == "}":
                self._write_token(class_body)
                break
            if class_body.value in CLASS_VAR_DECS:
                self._compile_class_var_dec(class_body)
            elif class_body.value in SUBROUTINE_DECS:
                self._compile_subroutine_dec(class_body)
        self._write("</class>\n")

    def _write(self, output):
        self.output_file.write((self.indent_level * INDENT) + output)

    def _write_token(self, token: Token):
        self.indent_level += 1
        tag = TOKEN_TAGS[token.token_type]
        self.output_file.write((self.indent_level * INDENT) +
                               f"<{tag}> {html.escape(token.value)} </{tag}>\n")
        self.indent_level -= 1

    def _next_token(self, *, values=[], token_types=[]):
        if self.tokenizer.has_more_tokens():
            token = self.tokenizer.pop_next_token()
            if values:
                if token.value in values:
                    return token
                raise Exception(
                    f"Token value {token.value} does not match expected values: {values}")
            if token_types:
                if token.token_type in token_types:
                    return token
                raise Exception(
                    f"Token value {token.token_type} does not match expected types: {token_types}")
            return token

        raise NoMoreTokensException("No more tokens")

    def _compile_class_var_dec(self, entry_token):
        self.indent_level += 1
        self._write("<classVarDec>\n")
        self._write_token(entry_token)
        type_declaration = self._next_token()
        if type_declaration.value not in ["int", "char", "boolean"] and type_declaration.token_type != TokenType.IDENTIFIER:
            raise Exception(
                f"Syntax error: expected type declaration but got {type_declaration}")
        self._write_token(type_declaration)
        while True:
            identifier = self._next_token(token_types=[TokenType.IDENTIFIER])
            self._write_token(identifier)
            next_token = self._next_token(values=[",", ";"])
            self._write_token(next_token)
            if next_token.value == ";":
                break
        self._write("</classVarDec>\n")
        self.indent_level -= 1

    def _compile_var_dec(self, entry_token):
        self.indent_level += 1
        self._write("<varDec>\n")
        self._write_token(entry_token)
        type_declaration = self._next_token()
        if type_declaration.value not in ["int", "char", "boolean"] and type_declaration.token_type != TokenType.IDENTIFIER:
            raise Exception(
                f"Syntax error: expected type declaration but got {type_declaration}")
        self._write_token(type_declaration)
        while True:
            identifier = self._next_token(token_types=[TokenType.IDENTIFIER])
            self._write_token(identifier)
            next_token = self._next_token(values=[",", ";"])
            self._write_token(next_token)
            if next_token.value == ";":
                break
        self._write("</varDec>\n")
        self.indent_level -= 1

    def _compile_subroutine_dec(self, entry_token):
        self.indent_level += 1
        self._write("<subroutineDec>\n")
        self._write_token(entry_token)
        type_declaration = self._next_token()
        if type_declaration.value not in ["int", "char", "boolean", "void"] and type_declaration.token_type != TokenType.IDENTIFIER:
            raise Exception(
                f"Syntax error: expected type declaration but got {type_declaration}")
        self._write_token(type_declaration)
        routine_name = self._next_token(token_types=[TokenType.IDENTIFIER])
        self._write_token(routine_name)
        opening_bracket = self._next_token(values=["("])
        self._write_token(opening_bracket)
        closing_bracket = self._compile_parameter_list()
        self._write_token(closing_bracket)

        opening_curly_bracket = self._next_token(values=["{"])
        self._compile_subroutine_body(opening_curly_bracket)

        self._write("</subroutineDec>\n")
        self.indent_level -= 1
        # self._write_token(closing_curly_bracket)

    def _compile_parameter_list(self):
        self.indent_level += 1
        self._write("<parameterList>\n")
        while True:
            next_token = self._next_token(values=[")", ",", "int", "char", "boolean"])
            if next_token.value == ")":
                break
            elif next_token.value == ",":
                self._write_token(next_token)
            else:
                self._write_token(next_token)
                arg_name = self._next_token(token_types=[TokenType.IDENTIFIER])
                self._write_token(arg_name)
        self._write("</parameterList>\n")
        self.indent_level -= 1
        return next_token

    def _compile_subroutine_body(self, entry_token):
        self.indent_level += 1
        self._write("<subroutineBody>\n")
        self._write_token(entry_token)
        while True:
            next_token = self._next_token()
            if next_token.value == "}":
                break
            if next_token.value == "var":
                self._compile_var_dec(next_token)
            elif next_token.value in STATEMENTS:
                self._write_token(self._compile_statements(next_token))
                break
        self._write("</subroutineBody>\n")
        self.indent_level -= 1
        return next_token

    def _compile_statements(self, entry_token):
        """Compiles a subroutine and returns the enclosing curly bracket token"""
        self.indent_level += 1
        self._write("<statements>\n")
        next_token = entry_token
        while True:
            if next_token.value == "}":
                break
            elif next_token.value == "let":
                self._compile_let_statement(next_token)
            elif next_token.value == "if":
                self._compile_if_statement(next_token)
            elif next_token.value == "while":
                self._compile_while_statement(next_token)
            elif next_token.value == "do":
                self._compile_do_statement(next_token)
            elif next_token.value == "return":
                self._compile_return_statement(next_token)
            next_token = self._next_token(values=[*STATEMENTS, "}"])

        self._write("</statements>\n")
        self.indent_level -= 1
        return next_token

    def _compile_let_statement(self, entry_token):
        self.indent_level += 1
        self._write("<letStatement>\n")
        self._write_token(entry_token)
        var_name = self._next_token(token_types=[TokenType.IDENTIFIER])
        self._write_token(var_name)
        next_token = self._next_token(values=["[", "="])
        self._write_token(next_token)
        if next_token.value == "[":
            closing_bracket = self._compile_expression()
            self._write_token(closing_bracket)
            assignment = self._next_token(values=["="])
            self._write_token(assignment)
        semicolon = self._compile_expression()
        self._write_token(semicolon)
        self._write("</letStatement>\n")
        self.indent_level -= 1

    def _compile_if_statement(self, entry_token):
        self.indent_level += 1
        self._write("<ifStatement>\n")
        self._write_token(entry_token)
        self._write_token(self._next_token(values=["("]))
        closing_bracket = self._compile_expression()
        self._write_token(closing_bracket)
        self._write_token(self._next_token(values=["{"]))
        closing_curly_bracket = self._compile_statements(
            self._next_token(values=[*STATEMENTS]))
        self._write_token(closing_curly_bracket)
        if self._peek().value == "else":
            self._write_token(self._next_token())
            self._write_token(self._next_token(values=["{"]))
            closing_curly_bracket = self._compile_statements(
                self._next_token(values=[*STATEMENTS]))
            self._write_token(closing_curly_bracket)

        self._write("</ifStatement>\n")
        self.indent_level -= 1

    def _compile_while_statement(self, entry_token):
        self.indent_level += 1
        self._write("<whileStatement>\n")
        self._write_token(entry_token)
        self._write_token(self._next_token(values=["("]))
        closing_bracket = self._compile_expression()
        self._write_token(closing_bracket)
        self._write_token(self._next_token(values=["{"]))
        closing_curly_bracket = self._compile_statements(
            self._next_token(values=[*STATEMENTS]))
        self._write_token(closing_curly_bracket)
        self._write("</whileStatement>\n")
        self.indent_level -= 1

    def _compile_do_statement(self, entry_token):
        self.indent_level += 1
        self._write("<doStatement>\n")
        self._write_token(entry_token)
        self._write_token(self._next_token(token_types=[TokenType.IDENTIFIER]))
        next_token = self._next_token(values=["(", "."])
        self._write_token(next_token)
        if next_token.value == ".":
            self._write_token(self._next_token(
                token_types=[TokenType.IDENTIFIER]))
            self._write_token(self._next_token(values=["("]))
        closing_bracket = self._compile_expression_list()
        self._write_token(closing_bracket)
        self._write_token(self._next_token(values=[";"]))
        self._write("</doStatement>\n")
        self.indent_level -= 1

    def _compile_return_statement(self, entry_token):
        self.indent_level += 1
        self._write("<returnStatement>\n")
        self._write_token(entry_token)
        next_token = self._peek()
        if next_token.value != ";":
            return_token = self._compile_expression()
            self._write_token(return_token)
        else:
            self._write_token(self._next_token())
        self._write("</returnStatement>\n")
        self.indent_level -= 1

    def _compile_expression(self):
        """Returns terminal token that signals the end of the expression"""
        self.indent_level += 1
        self._write("<expression>\n")
        self._compile_term()
        next_token = self._next_token(values=[*OPERATORS, ";", ")", "]", ","])
        while next_token.value in OPERATORS:
            self._write_token(next_token)
            self._compile_term()
            next_token = self._next_token(values=[*OPERATORS, ";", ")", "]", ","])
        self._write("</expression>\n")
        self.indent_level -= 1
        return next_token

    def _compile_term(self):
        """Compiles a term, no exit token"""
        self.indent_level += 1
        self._write("<term>\n")
        next_token = self._peek()
        if next_token.token_type in {TokenType.INT_CONST, TokenType.STRING_CONST}:
            self._write_token(self._next_token())
        elif next_token.value in KEYWORD_CONST:
            self._write_token(self._next_token())
        elif next_token.value in UNARY_OPS:
            self._write_token(self._next_token())
            self._compile_term()
        elif next_token.value == "(":
            self._write_token(self._next_token())
            self._write_token(self._compile_expression())
        elif next_token.token_type == TokenType.IDENTIFIER:
            self._write_token(self._next_token())
            next_token = self._peek()
            if next_token.value == "[":
                self._write_token(self._next_token())
                self._write_token(self._compile_expression())
            if next_token.value == "(":
                self._write_token(self._next_token())
                self._write_token(self._compile_expression_list())
            if next_token.value == ".":
                self._write_token(self._next_token())
                self._write_token(self._next_token(
                    token_types=[TokenType.IDENTIFIER]))
                self._write_token(self._next_token(values=["("]))
                self._write_token(self._compile_expression_list())

        self._write("</term>\n")
        self.indent_level -= 1

    def _compile_expression_list(self):
        """Compile a list of expressions and returns the terminal token"""
        self.indent_level += 1
        self._write("<expressionList>\n")
        next_token = self._peek()
        if next_token.value == ")":
            self._write("</expressionList>\n")
            self.indent_level -= 1
            return self._next_token()
        return_token = self._compile_expression()
        while return_token.value == ",":
            self._write_token(return_token)
            return_token = self._compile_expression()
        self._write("</expressionList>\n")
        self.indent_level -= 1
        return return_token

    def _peek(self) -> Token:
        if self.tokenizer.has_more_tokens():
            return Token(self.tokenizer.tokens[0])
        raise NoMoreTokensException()


class NoMoreTokensException(Exception):
    """ Raises an exception if the CompileEngine requests a token """
