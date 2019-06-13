#!/usr/bin/env python3
import sys, os
from typing import TextIO
from arithmetic_ops import ARITHMETIC_OPS, TRUE, FALSE
from memory import STACK_OPS

SPR  = 0
LCL  = 1
ARG  = 2
THIS = 3
THAT = 4

filename = sys.argv[1]
output = filename.split(".")[0]
output_file = output + ".asm"
base = output.split("/")[-1]

def parse_line(line):
    commands = []
    command = ""
    for char in line:
        if char == "/" or char == "\n":
            if command:
                commands.append(command)
            break
        if char == " ":
            commands.append(command)
            command = ""
        else:
            command += char
    return commands

# Initialize true and false branches and jumps to start of program
INITIALIZE = "@START\n    0;JMP\n" + TRUE + FALSE + "(START)\n"
END = "(END)\n    @END\n    0;JMP\n"

with open(filename) as f:
    with open(output_file, "w") as o:
        o.write(INITIALIZE)
        for line in f:
            commands = parse_line(line)
            if len(commands) == 3:
                o.write(STACK_OPS[commands[0]](commands[1], commands[2], base))
            elif len(commands) == 1:
                o.write(ARITHMETIC_OPS[commands[0]]())
            else:
                continue
        o.write(END)