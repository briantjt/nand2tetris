SPR = 0
LCL = 1
ARG = 2
THIS = 3
THAT = 4


pop_second_arg = f"    @{SPR}\n" \
    "    M=M-1\n" \
    "    A=M\n" \
    "    D=M\n"

advance_spr = f"    @{SPR}\n" \
    "    M=M+1\n"

get_first_arg = f"    @{SPR}\n" \
    "    M=M-1\n" \
    "    A=M\n"

def ADD():
    return pop_second_arg + \
    get_first_arg + \
    "    MD=D+M\n" + \
    advance_spr


def SUB():
    return pop_second_arg + \
    get_first_arg + \
    "    MD=M-D\n" + \
    advance_spr

def NEG():
    return get_first_arg + \
    "    M=-M\n" + \
    advance_spr

def AND():
    return pop_second_arg + \
    get_first_arg + \
    "    M=D&M\n" + \
    advance_spr

def OR():
    return pop_second_arg + \
    get_first_arg + \
    "    M=D|M\n" + \
    advance_spr

def NOT():
    return get_first_arg + \
    "    M=!M\n" + \
    advance_spr

TRUE = "(TRUE)\n" \
    f"    @{SPR}\n" \
    "    A=M\n" \
    "    M=-1\n" \
    f"    @{SPR}\n" \
    f"    M=M+1\n" \
    "    @R15\n" \
    "    A=M\n" \
    "    0;JMP\n"

FALSE = "(FALSE)\n" \
    f"    @{SPR}\n" \
        "    A=M\n" \
        "    M=0\n" \
    f"    @{SPR}\n" \
    f"    M=M+1\n" \
        "    @R15\n" \
        "    A=M\n" \
        "    0;JMP\n"


def eq_label():
    n = 1
    while True:
        yield n
        n += 1


eq_label = eq_label()


def EQ():
    n = next(eq_label)
    return f"    @EQ_{n}\n" \
           f"    D=A\n" \
           f"    @R15\n" \
           f"    M=D\n" + \
           pop_second_arg + \
           get_first_arg + \
            "    D=M-D\n" \
            "    @TRUE\n" \
            "    D;JEQ\n" \
            "    @FALSE\n" \
            "    0;JMP\n" \
           f"(EQ_{n})\n"


def gt_label():
    n = 1
    while True:
        yield n
        n += 1


gt_label = gt_label()


def GT():
    n = next(gt_label)
    return f"    @GT_{n}\n" \
        f"    D=A\n" \
        f"    @R15\n" \
        f"    M=D\n" + \
        pop_second_arg + \
        get_first_arg + \
        "    D=M-D\n" \
        "    @TRUE\n" \
        "    D;JGT\n" \
        "    @FALSE\n" \
        "    0;JMP\n" \
        f"(GT_{n})\n"


def lt_label():
    n = 1
    while True:
        yield n
        n += 1


lt_label = lt_label()


def LT():
    n = next(lt_label)
    return f"    @LT_{n}\n" \
        f"    D=A\n" \
        f"    @R15\n" \
        f"    M=D\n" + \
        pop_second_arg + \
        get_first_arg + \
        "    D=M-D\n" \
        "    @TRUE\n" \
        "    D;JLT\n" \
        "    @FALSE\n" \
        "    0;JMP\n" \
        f"(LT_{n})\n"


ARITHMETIC_OPS = {
    "add": ADD,
    "sub": SUB,
    "neg": NEG,
    "and": AND,
    "or": OR,
    "not": NOT,
    "gt": GT,
    "lt": LT,
    "eq": EQ
}
