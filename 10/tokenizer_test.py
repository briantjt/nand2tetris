#!/usr/bin/env python3

from compiler.tokenizer import Tokenizer
from compiler.tokens import TOKEN_TAGS
import sys
import os
import html

ARG = sys.argv[1]
if os.path.isfile(ARG):
    FILES = [ARG]
else:
    FILES = [os.path.abspath(ARG) + "/" +
             f for f in os.listdir(ARG) if f.endswith('.jack')]

for f in FILES:
    output_filename = os.path.abspath(f).split('.')[0] + 'Z.xml'
    output_file = open(output_filename, "w")
    tokenizer = Tokenizer(f)
    output_file.write("<tokens>\n")

    while tokenizer.has_more_tokens():
        token = tokenizer.pop_next_token()
        tag = TOKEN_TAGS[token.token_type]
        output_file.write(f"<{tag}> {html.escape(token.value)} </{tag}>\n")

    output_file.write("</tokens>\n")
    tokenizer.close_file()
    output_file.close()
