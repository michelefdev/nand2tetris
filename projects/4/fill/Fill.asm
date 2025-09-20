// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

@KBD
D=A
@kbdaddress
M=D

    (LISTEN)
    @SCREEN
    D=A
    @pointer 
    M=D

    @KBD
    D=M

    @WHITE
    D;JEQ

    @BLACK
    0;JMP


        (BLACK)
        @pointer
        A=M
        M=-1

        D=A
        @kbdaddress
        D=M-D

        @LISTEN
        D;JEQ

        @pointer
        M=M+1

        @BLACK
        0;JMP


        (WHITE)
        @pointer
        A=M
        M=-1

        D=A
        @kbdaddress
        D=M-D

        @LISTEN
        D;JEQ

        @pointer
        M=M+1

        @WHITE
        0;JMP


    (END)
    @END
    0;JMP