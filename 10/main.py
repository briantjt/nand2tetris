#!/usr/bin/env python3

from compiler.tokenizer import Tokenizer
from compiler.tokens import TOKEN_TAGS
import sys
import os
import html

arg = sys.argv[1]
if os.path.isfile(arg):
    files = [arg]
else:
    files = [os.path.abspath(arg) + "/" + f for f in os.listdir(arg) if f.endswith('.jack')]

for f in files:
    output_filename = os.path.abspath(f).split('.')[0] + 'T.xml'
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
