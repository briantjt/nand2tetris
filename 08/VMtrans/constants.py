import sys, os

SPR = 0
LCL = 1
ARG = 2
THIS = 3
THAT = 4
TEMP = 5

pop_second_arg = f"    @{SPR}\n" \
                  "    M=M-1\n" \
                  "    A=M\n" \
                  "    D=M\n"

advance_spr = f"    @{SPR}\n" \
               "    M=M+1\n"

get_first_arg = f"    @{SPR}\n" \
                 "    M=M-1\n" \
                 "    A=M\n"

