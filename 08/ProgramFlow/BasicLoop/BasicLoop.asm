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
    @0
    D=A
    @0
    A=M
    M=D
    @0
    M=M+1
    @0
    D=A
    @1
    D=M+D
    @R14
    M=D
    @0
    AM=M-1
    D=M
    @R14
    A=M
    M=D
(LOOP_START)
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
    D=A
    @1
    D=M+D
    @R14
    M=D
    @0
    AM=M-1
    D=M
    @R14
    A=M
    M=D
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
    @0
    D=A
    @2
    D=M+D
    @R14
    M=D
    @0
    AM=M-1
    D=M
    @R14
    A=M
    M=D
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
    @LOOP_START
    D; JNE
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
(END)
    @END
    0;JMP