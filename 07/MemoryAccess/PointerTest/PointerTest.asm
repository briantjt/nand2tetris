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
    @3030
    D=A
    @0
    A=M
    M=D
    @0
    M=M+1
    @0
    AM=M-1
    D=M
    @3
    M=D
    @3040
    D=A
    @0
    A=M
    M=D
    @0
    M=M+1
    @0
    AM=M-1
    D=M
    @4
    M=D
    @32
    D=A
    @0
    A=M
    M=D
    @0
    M=M+1
    @2
    D=A
    @3
    D=M+D
    @R14
    M=D
    @0
    AM=M-1
    D=M
    @R14
    A=M
    M=D
    @46
    D=A
    @0
    A=M
    M=D
    @0
    M=M+1
    @6
    D=A
    @4
    D=M+D
    @R14
    M=D
    @0
    AM=M-1
    D=M
    @R14
    A=M
    M=D
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
    M=M-1
    A=M
    D=M
    @0
    M=M-1
    A=M
    M=M+D
    @0
    M=M+1
    @2
    D=A
    @3
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
    @6
    D=A
    @4
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
(END)
    @END
    0;JMP
