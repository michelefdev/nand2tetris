// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.


(FIRST_LISTEN)
@KBD
D=M

@FIRST_WHITE
D;JEQ

@FIRST_BLACK
0;JMP

	(FIRST_WHITE)
	@SCREEN
	M=0
	D=A
	D=D+1
	@LISTEN
	0;JMP


	(FIRST_BLACK)
	@SCREEN
	M=-1
	D=A
	D=D+1
	@LISTEN
	0;JMP

	(LISTEN)
	@pointer
	M=D

	@KBD
	D=M

	@LOOP_WHITE
	D;JEQ

	@LOOP_BLACK
	0;JMP

		(LOOP_WHITE)
		@pointer
		A=M
		M=0
		D=A
		D=D+1
		@pointer
		M=D

		@KBD
		D=M
		@LOOP_WHITE
		D;JEQ

		@FIRST_BLACK
		0;JMP

		(LOOP_BLACK)
		@pointer
		A=M
		M=-1
		D=A
		D=D+1
		@pointer
		M=D

		@KBD
		D=M

		@FIRST_WHITE
		D;JEQ

		@LOOP_BLACK
		0;JMP