SPR = 0
LCL = 1
ARG = 2
THIS = 3
THAT = 4
TEMP = 5

scoped_segments = {
    "local": LCL,
    "argument": ARG,
    "this": THIS,
    "that": THAT,
}

pointer = {
    "0": f"{THIS}",
    "1": f"{THAT}"
}

def push_stack(mem_segment: str, mem_index: str, base: str):
    if mem_segment == "constant":
        return f"    @{mem_index}\n" \
                "    D=A\n" \
               f"    @{SPR}\n" \
                "    A=M\n" \
                "    M=D\n" \
               f"    @{SPR}\n" \
                "    M=M+1\n"
    elif mem_segment == "static":
        return f"    @{base}.{mem_index}\n" \
                "    D=M\n" \
               f"    @{SPR}\n" \
               f"    A=M\n" \
               f"    M=D\n" \
               f"    @{SPR}\n" \
               f"    M=M+1\n"
    elif mem_segment == "temp":
        return f"    @{5 + int(mem_index)}\n" \
                "    D=M\n" \
               f"    @{SPR}\n" \
               f"    A=M\n" \
               f"    M=D\n" \
               f"    @{SPR}\n" \
               f"    M=M+1\n"
    elif mem_segment == "pointer":
       return  f"    @{pointer[mem_index]}\n" \
                "    D=M\n" \
               f"    @{SPR}\n" \
                "    A=M\n" \
                "    M=D\n" \
               f"    @{SPR}\n" \
               f"    M=M+1\n"
    # For local, argument, this, that
    elif mem_segment in scoped_segments:
        return f"    @{mem_index}\n" \
                "    D=A\n" \
               f"    @{scoped_segments[mem_segment]}\n" \
                "    A=M+D\n" \
                "    D=M\n" \
               f"    @{SPR}\n" \
                "    A=M\n" \
                "    M=D\n" \
               f"    @{SPR}\n" \
                "    M=M+1\n"

def pop_stack(mem_segment, mem_index, base):
    if mem_segment == "static":
        return f"    @{SPR}\n" \
                "    AM=M-1\n" \
                "    D=M\n" \
               f"    @{base}.{mem_index}\n" \
                "    M=D\n"
    elif mem_segment == "temp":
        return f"    @{SPR}\n" \
                "    AM=M-1\n" \
                "    D=M\n" \
               f"    @{5 + int(mem_index)}\n" \
                "    M=D\n"
    elif mem_segment == "pointer":
        return f"    @{SPR}\n" \
                "    AM=M-1\n" \
                "    D=M\n" \
               f"    @{pointer[mem_index]}\n" \
                "    M=D\n"
    else:
        return f"    @{mem_index}\n" \
                "    D=A\n" \
               f"    @{scoped_segments[mem_segment]}\n" \
                "    D=M+D\n" \
                "    @R14\n" \
                "    M=D\n" \
               f"    @{SPR}\n" \
                "    AM=M-1\n" \
                "    D=M\n" \
                "    @R14\n" \
                "    A=M\n" \
                "    M=D\n"

STACK_OPS = {
    "push": push_stack,
    "pop": pop_stack
}