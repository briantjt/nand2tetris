#!/usr/bin/env python3

from compiler.tokenizer import Tokenizer
from compiler.compileengine import CompilationEngine
import sys
import os

ARG = sys.argv[1]
if os.path.isfile(ARG):
    FILES = [ARG]
else:
    FILES = [os.path.abspath(ARG) + "/" +
             f for f in os.listdir(ARG) if f.endswith('.jack')]

for f in FILES:
    output_filename = os.path.abspath(f).split('.')[0] + 'E.xml'
    tokenizer = Tokenizer(f)
    compiler = CompilationEngine(output_filename, tokenizer)
    compiler.compile_class()
    tokenizer.close_file()
    compiler.close_file()
