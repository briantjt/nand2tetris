#!/usr/bin/env python3
import sys, os
from typing import TextIO
from arithmetic_ops import ARITHMETIC_OPS, TRUE, FALSE

SPR  = 0
LCL  = 1
ARG  = 2
THIS = 3
THAT = 4

filename = sys.argv[1]
base = filename.split(".")[0]
output_file = base + ".asm"

def manipulate_stack(action: str, mem_segment: str, mem_index: str):
    if action == "push":
        if mem_segment == "constant":
            return f"    @{mem_index}\n" \
                    "    D=A\n" \
                   f"    @{SPR}\n" \
                    "    A=M\n" \
                    "    M=D\n" \
                   f"    @{SPR}\n" \
                    "    M=M+1\n"
    else:
        pass


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
            print(commands)
            if len(commands) == 3:
                o.write(manipulate_stack(*commands))
            elif len(commands) == 1:
                o.write(ARITHMETIC_OPS[commands[0]]())
            else:
                continue
        o.write(END)