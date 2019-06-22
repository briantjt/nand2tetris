from constants import *
from memory import push_stack, pop_stack

return_count = 1

push_and_adv_pointer = f"    @{SPR}\n" \
                        "    A=M\n" \
                        "    M=D\n" \
                       f"    @{SPR}\n" \
                        "    M=M+1\n" 

push_arg = f"    @{ARG}\n    D=M\n" + push_and_adv_pointer
push_lcl = f"    @{LCL}\n    D=M\n" + push_and_adv_pointer
push_this = f"    @{THIS}\n    D=M\n" + push_and_adv_pointer
push_that = f"    @{THAT}\n    D=M\n" + push_and_adv_pointer
offset = f"    @{SPR}\n    D=M\n    @5\n    D=D-A\n"
set_lcl = f"    @{SPR}\n    D=M\n    @{LCL}\n    M=D\n"

def call(function_name, args, base):
    global return_count
    return_label = f"{base}.ret.{return_count}"

    push_return_label = f"    @{return_label}\n" + \
                         "    D=A\n" + \
                         push_and_adv_pointer
    jump_to_func = f"    @{function_name}\n    0;JMP\n"
    
    set_args = offset + f"    @{args}\n    D=D-A\n    @{ARG}\n    M=D\n"
    return_count += 1
    return push_return_label + \
        push_lcl + \
        push_arg + \
        push_this + \
        push_that + \
        set_args + \
        set_lcl + \
        jump_to_func + \
        f"({return_label})\n"

def function(function_name, args):
    args = int(args)
    set_local = ""
    for i in range(args):
        set_local += "    @0\n    D=A\n" + push_and_adv_pointer
    return f"({function_name})\n" + \
        set_local

def f_return():
    save_Endframe = f"    @{LCL}\n" \
                     "    D=M\n" \
                     "    @Endframe\n" \
                     "    M=D\n" 
    save_return_address = "    @5\n" \
                          "    D=D-A\n" \
                          "    A=D\n" \
                          "    D=M\n" \
                          "    @R13\n" \
                          "    M=D\n"
    pop_return_value = f"    @{SPR}\n" \
                        "    AM=M-1\n" \
                        "    D=M\n" \
                       f"    @{ARG}\n" \
                        "    A=M\n" \
                        "    M=D\n"
    reposition_spr = f"    @{ARG}\n" \
                      "    D=M+1\n" \
                     f"    @{SPR}\n" \
                      "    M=D\n" 
    reposition_that = "    @Endframe\n" \
                      "    AM=M-1\n" \
                      "    D=M\n" \
                     f"    @{THAT}\n" \
                      "    M=D\n"
    reposition_this = "    @Endframe\n" \
                      "    AM=M-1\n" \
                      "    D=M\n" \
                     f"    @{THIS}\n" \
                      "    M=D\n"
    reposition_arg = "    @Endframe\n" \
                     "    AM=M-1\n" \
                     "    D=M\n" \
                    f"    @{ARG}\n" \
                     "    M=D\n"
    reposition_lcl = "    @Endframe\n" \
                     "    AM=M-1\n" \
                     "    D=M\n" \
                    f"    @{LCL}\n" \
                     "    M=D\n"
    goto_return_add = "    @R13\n" \
                      "    A=M\n" \
                      "    0;JMP\n"
    return save_Endframe + \
        save_return_address + \
        pop_return_value + \
        reposition_spr + \
        reposition_that + \
        reposition_this + \
        reposition_arg + \
        reposition_lcl + \
        goto_return_add

FUNC_OPS = {
    "function": function,
    "call": call,
    "return": f_return
}