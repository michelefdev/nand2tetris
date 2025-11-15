# 🖥️ *From Logic Gates to a Working Computer* — Nand2Tetris Study Journey

> “The best way to understand a system is to build one.” — Nand2Tetris

This repository documents my progress through the **first six chapters of the Nand2Tetris course**.  
In this phase, I built core hardware components from **first principles**, using nothing but the **NAND gate** as the fundamental building block. Each chapter includes notes, HDL implementations, test results, and conceptual summaries.

## 🧭 Overview

**Nand2Tetris** is a project-based computer science course that guides you through constructing a computer system from scratch.  
The first six chapters focus on the hardware layer — building up from logic gates to a fully-functional **CPU and computer platform**.

You start with *boolean logic*, then build:
- Logic gates and combinational chips  
- Arithmetic components  
- Sequential chips with memory  
- The ALU  
- The CPU  
- A complete hardware platform capable of running machine code  

## 📚 Chapters & Key Achievements

| Chapter | Focus | Highlights |
|--------|--------|------------|
| 1 | Boolean Logic | Implemented basic logic gates (AND, OR, XOR, etc.) using only NAND; verified gates through provided test scripts |
| 2 | Boolean Arithmetic | Built adders, incrementer and ALU |
| 3 | Sequential Logic | Constructed flip-flops registersand a program counter, built RAM from lower-level memory elements |
| 4 | Machine LAnguage | Learned Hack machine instruction specification by writing small programs in Hack assembly and ran them in the CPU emulator |
| 5 | Computer Architecture | Integrated CPU, instruction memory and working memory into a computer capable of running 16 bits instructions |
| 6 | Assembler| Connected CPU, memory, and ROM into a full computer platform; successfully ran programs end-to-end |

## 🧩 What This Phase Builds

By the end of Chapter 6, I now have a complete **Hack Computer**, capable of:
- Executing arithmetic and logical operations
- Storing and retrieving values in memory
- Running assembly-level programs

This lays the groundwork for the next phase:
> **Writing an assembler, VM, compiler, and building a full operating system.**
