@START
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
(SimpleFunction.test)
    @1
    A=M
    M=0
    A=A+1
    M=0
    @0
    D=A
    @1
    A=M+D
    D=M
    @0
    A=M
    M=D
    @0
    M=M+1
    @1
    D=A
    @1
    A=M+D
    D=M
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
    M=M+D
    @0
    M=M+1
    @0
    M=M-1
    A=M
    M=!M
    @0
    M=M+1
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
    D=A
    @2
    A=M+D
    D=M
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
(END)
    @END
    0;JMP
