# Hack Assembler (Generated with `copilot.med`)

A compact Hack Assembler for Nand2Tetris, generated using a structured
`assembler_copilot.md` file to guide GitHub Copilot.

## Features
-   Converts `.asm` to `.hack`
-   Supports A- and C-instructions
-   No symbol resolution (yet)
-   Matches official Nand2Tetris outputs

## Usage
    hack-assembler input.asm output.hack

## Files
-   `assembler_copilot.md` -- prompt file used to generate the assembler \
-   `*.py` -- source code \

## Notes
-   The program worked right out of the box, there was no need to tweak copilot output.
-   I used it with `python assembler.py input.asm` where the input were the *.asm programs contained in the add, max, and pong folders. Then I compared the output with the one produced by the provided assembler and all comparisons were successfull