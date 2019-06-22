#!/usr/bin/env python3
import sys, os
from typing import TextIO
from arithmetic_ops import ARITHMETIC_OPS, TRUE, FALSE
from memory import STACK_OPS
from branches import BRANCH_OPS
from functions import FUNC_OPS

OPS = {**STACK_OPS, **BRANCH_OPS, **FUNC_OPS, **ARITHMETIC_OPS}

filename_req = { "call", "push", "pop" }
path = sys.argv[-1]
abs_path = os.path.abspath(path)
if os.path.isdir(path):
    output_file = abs_path + "/" + os.path.basename(path) + ".asm"
    files = [abs_path + "/" + f for f in os.listdir(path) if ".vm" in f]
else:
    files = [abs_path + path]
    output = path.split(".")[0]
    output_file = output + ".asm"

def parse_line(line):
    commands = []
    command = ""
    for char in line:
        if char == "/" or char == "\n":
            if command:
                commands.append(command)
            break
        if char == " ":
            if command:
                commands.append(command)
                command = ""
        else:
            command += char
    return commands

# Initialize true and false branches and jumps to start of program
INITIALIZE = "    @START\n    0;JMP\n" + TRUE + FALSE + "(START)\n"
END = "(END)\n    @END\n    0;JMP\n"

with open(output_file, "w") as o:
    if os.path.isdir(path):
        o.write(OPS["call"]("Sys.init", 0, os.path.basename(path)))
    o.write(INITIALIZE)
    for fi in files:
        with open(fi) as f:
            base = fi.split("/")[-1].split(".vm")[0]
            for line in f:
                commands = parse_line(line)
                if not commands:
                    continue
                elif commands[0] in filename_req:
                    o.write(OPS[commands[0]](*commands[1:], base))
                else:
                    o.write(OPS[commands[0]](*commands[1:]))
    o.write(END)
