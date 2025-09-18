// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// The algorithm is based on repetitive addition.

@R2
M=0

@i
M=0

(LOOP)
@i
D=M     // D = i
@R1
D=M-D 	// D = R1 - i

@END  	// if R1 - i = 0 then R1=i then program ends
D;JEQ

@R0	    // otherwise add R0 to the total stored in R2 ...
D=M

@R2
M=M+D

@i
M=M+1   // increment i

@LOOP	// ... and jump back to the top of the loop
0;JMP

(END)   // End of program
@END
0;JMP
