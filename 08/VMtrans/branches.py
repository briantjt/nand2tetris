from constants import *

def label(name):
    return f"    ({name})\n"

def if_goto(name):
    return pop_second_arg + \
           f"    @{name}\n" \
            "    D; JNE\n"

def goto(name):
    return f"    @{name}\n" \
            "    0; JMP\n"

BRANCH_OPS = {
    "label": label,
    "goto": goto,
    "if-goto": if_goto
}