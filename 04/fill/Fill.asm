// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
(LISTEN)
    @SCREEN
    D = A
    @j // Reset memory location to start of screen
    M = D
    @KBD
    D = M
    @CLEAR
    D; JEQ
    @FILL
    0; JMP
(CLEAR)
    @j
    A = M
    M = 0
    @j
    M = M + 1
    D = M
    @24576
    D = D - A
    @CLEAR
    D; JLT
    @LISTEN
    0; JMP
(FILL)
    @j
    A = M
    M = -1
    @j
    M = M + 1
    D = M
    @24576
    D = D - A
    @FILL
    D; JLT
    @LISTEN
    0; JMP