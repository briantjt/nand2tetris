    @Sys.init
    0;JMP
(TRUE)
    @0
    A=M
    M=-1
    @0
    M=M+1
    @R15
    A=M
    0;JMP
(FALSE)
    @0
    A=M
    M=0
    @0
    M=M+1
    @R15
    A=M
    0;JMP
(START)
(Main.fibonacci)
    @0
    D=A
    @2
    A=M+D
    D=M
    @0
    A=M
    M=D
    @0
    M=M+1
    @2
    D=A
    @0
    A=M
    M=D
    @0
    M=M+1
    @LT_1
    D=A
    @R15
    M=D
    @0
    M=M-1
    A=M
    D=M
    @0
    M=M-1
    A=M
    D=M-D
    @TRUE
    D;JLT
    @FALSE
    0;JMP
(LT_1)
    @0
    M=M-1
    A=M
    D=M
    @IF_TRUE
    D; JNE
@IF_FALSE
    0; JMP
(IF_TRUE)
    @0
    D=A
    @2
    A=M+D
    D=M
    @0
    A=M
    M=D
    @0
    M=M+1
    @1
    D=M
    @Endframe
    M=D
    @5
    D=D-A
    A=D
    D=M
    @R13
    M=D
    @0
    AM=M-1
    D=M
    @2
    A=M
    M=D
    @2
    D=M+1
    @0
    M=D
    @Endframe
    AM=M-1
    D=M
    @4
    M=D
    @Endframe
    AM=M-1
    D=M
    @3
    M=D
    @Endframe
    AM=M-1
    D=M
    @2
    M=D
    @Endframe
    AM=M-1
    D=M
    @1
    M=D
    @R13
    A=M
    0;JMP
(IF_FALSE)
    @0
    D=A
    @2
    A=M+D
    D=M
    @0
    A=M
    M=D
    @0
    M=M+1
    @2
    D=A
    @0
    A=M
    M=D
    @0
    M=M+1
    @0
    M=M-1
    A=M
    D=M
    @0
    M=M-1
    A=M
    M=M-D
    @0
    M=M+1
    @Main.ret.1
    D=A
    @0
    A=M
    M=D
    @0
    M=M+1
    @1
    D=M
    @0
    A=M
    M=D
    @0
    M=M+1
    @2
    D=M
    @0
    A=M
    M=D
    @0
    M=M+1
    @3
    D=M
    @0
    A=M
    M=D
    @0
    M=M+1
    @4
    D=M
    @0
    A=M
    M=D
    @0
    M=M+1
    @0
    D=M
    @5
    D=D-A
    @1
    D=D-A
    @2
    M=D
    @0
    D=M
    @1
    M=D
    @Main.fibonacci
    0;JMP
(Main.ret.1)
    @0
    D=A
    @2
    A=M+D
    D=M
    @0
    A=M
    M=D
    @0
    M=M+1
    @1
    D=A
    @0
    A=M
    M=D
    @0
    M=M+1
    @0
    M=M-1
    A=M
    D=M
    @0
    M=M-1
    A=M
    M=M-D
    @0
    M=M+1
    @Main.ret.2
    D=A
    @0
    A=M
    M=D
    @0
    M=M+1
    @1
    D=M
    @0
    A=M
    M=D
    @0
    M=M+1
    @2
    D=M
    @0
    A=M
    M=D
    @0
    M=M+1
    @3
    D=M
    @0
    A=M
    M=D
    @0
    M=M+1
    @4
    D=M
    @0
    A=M
    M=D
    @0
    M=M+1
    @0
    D=M
    @5
    D=D-A
    @1
    D=D-A
    @2
    M=D
    @0
    D=M
    @1
    M=D
    @Main.fibonacci
    0;JMP
(Main.ret.2)
    @0
    M=M-1
    A=M
    D=M
    @0
    M=M-1
    A=M
    M=M+D
    @0
    M=M+1
    @1
    D=M
    @Endframe
    M=D
    @5
    D=D-A
    A=D
    D=M
    @R13
    M=D
    @0
    AM=M-1
    D=M
    @2
    A=M
    M=D
    @2
    D=M+1
    @0
    M=D
    @Endframe
    AM=M-1
    D=M
    @4
    M=D
    @Endframe
    AM=M-1
    D=M
    @3
    M=D
    @Endframe
    AM=M-1
    D=M
    @2
    M=D
    @Endframe
    AM=M-1
    D=M
    @1
    M=D
    @R13
    A=M
    0;JMP
(Sys.init)
    @4
    D=A
    @0
    A=M
    M=D
    @0
    M=M+1
    @Sys.ret.3
    D=A
    @0
    A=M
    M=D
    @0
    M=M+1
    @1
    D=M
    @0
    A=M
    M=D
    @0
    M=M+1
    @2
    D=M
    @0
    A=M
    M=D
    @0
    M=M+1
    @3
    D=M
    @0
    A=M
    M=D
    @0
    M=M+1
    @4
    D=M
    @0
    A=M
    M=D
    @0
    M=M+1
    @0
    D=M
    @5
    D=D-A
    @1
    D=D-A
    @2
    M=D
    @0
    D=M
    @1
    M=D
    @Main.fibonacci
    0;JMP
(Sys.ret.3)
(WHILE)
@WHILE
    0; JMP
(END)
    @END
    0;JMP
