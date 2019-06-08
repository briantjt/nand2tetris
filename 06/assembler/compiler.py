#!/usr/bin/env python3
import sys
import os

computations = {
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "!D": "0001101",
    "!A": "0110001",
    "-D": "0001111",
    "-A": "0110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "D+A": "0000010",
    "D-A": "0010011",
    "A-D": "0000111",
    "D&A": "0000000",
    "D|A": "0010101",
    "M": "1110000",
    "!M": "1110001",
    "-M": "1110011",
    "M+1": "1110111",
    "M-1": "1110010",
    "D+M": "1000010",
    "D-M": "1010011",
    "M-D": "1000111",
    "D&M": "1000000",
    "D|M": "1010101"
}


destinations = {
    "null": "000",
    "M": "001",
    "D": "010",
    "A": "100",
    "MD": "011",
    "AM": "101",
    "AD": "110",
    "AMD": "111"
}


jumps = {
    "null": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
}

symbols = {
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "R4": 4,
    "R5": 5,
    "R6": 6,
    "R7": 7,
    "R8": 8,
    "R9": 9,
    "R10": 10,
    "R11": 11,
    "R12": 12,
    "R13": 13,
    "R14": 14,
    "R15": 15,
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
    "SCREEN": 16384,
    "KBD": 24576,
}

asm_file = sys.argv[1]
base = asm_file.split(".")[0]
temp_file = base + ".tmp"
final_file = base + ".hack"
register_number = 16

def preprocess(line: str) -> str:
    line = line.split("//")[0].strip()
    if not line:
        return ""
    if line[0] == "/" or line[0] == "\n":
        return ""
    return line


def parse_symbol(line: str) -> str:
    symbol = ""
    for i in range(1, len(line)):
        if line[i] == ")":
            break
        symbol += line[i]
    return symbol

def compile_a_instruction(line: str) -> str:
    line = line.strip()
    address_length = 16
    address = line[1:]
    if address.isnumeric():
        address_code = format(int(address), 'b')
    else:
        if address in symbols:
            address_code = format(symbols[address], 'b')
        else:
            global register_number
            symbols[address] = register_number
            address_code = format(register_number, 'b')
            register_number += 1

    address_code = ("0" * (address_length - len(address_code))) + address_code
    return address_code

def compile_c_instruction(line: str) -> str:
    temp = line.strip().split("=")
    if len(temp) == 1:
        dest_code = destinations["null"]
    else:
        dest = temp[0]
        dest_code = destinations[dest]

    comp_and_jump = temp[-1].split(";")
    comp = "".join(comp_and_jump[0].strip().split(" "))
    comp_code = computations[comp]
    if len(comp_and_jump) == 1:
        jump_code = jumps["null"]
    else:
        jump_code = jumps[comp_and_jump[1]]
    
    return "111" + comp_code + dest_code + jump_code
    

def parse_symbols():
    with open(asm_file) as f:
        with open(temp_file, "w") as temp:
            line_number = 0
            for line in f:
                preprocessed_line = preprocess(line)
                if not preprocessed_line:
                    continue
                if preprocessed_line[0] == "(":
                    symbol = parse_symbol(preprocessed_line)
                    symbols[symbol] = line_number
                else:
                    line_number += 1
                    temp.write(preprocessed_line + "\n")


def compile():
    with open(temp_file) as f:
        with open(final_file, "w") as o:
            for line in f:
                if line[0] == "@":
                    o.write(compile_a_instruction(line) + "\n")
                else:
                    o.write(compile_c_instruction(line) + "\n")

    os.remove(temp_file)

if __name__ == "__main__":
    parse_symbols()
    compile()
