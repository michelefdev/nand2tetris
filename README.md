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

| Chapter | Focus | Status | Highlights |
|--------|--------|--------|------------|
| 1 | Boolean Logic | ✅ Completed | Implemented basic logic gates (AND, OR, XOR, etc.) using only NAND; verified gates through provided test scripts |
| 2 | Combinational Chips | ✅ Completed | Built multiplexers, demultiplexers, adders, and ALU components; designed multi-bit logic using composition |
| 3 | Sequential Logic | ✅ Completed | Constructed flip-flops and registers; introduced clocked circuits; built RAM from lower-level memory elements |
| 4 | Machine-Level Instructions | ✅ Completed | Learned Hack machine instruction specification; wrote small programs in Hack assembly and ran them in the CPU emulator |
| 5 | The Hack CPU | ✅ Completed | Integrated ALU and control logic to design a working CPU capable of executing instructions |
| 6 | The Hack Computer | ✅ Completed | Connected CPU, memory, and ROM into a full computer platform; successfully ran programs end-to-end |

## 🧩 What This Phase Builds

By the end of Chapter 6, I now have a complete **Hack Computer**, capable of:
- Executing arithmetic and logical operations
- Storing and retrieving values in memory
- Running assembly-level programs

This lays the groundwork for the next phase:
> **Writing an assembler, VM, compiler, and building a full operating system.**

## 🗂️ Repository Contents

```
/
├─ 01-boolean-logic/
├─ 02-combinational-chips/
├─ 03-sequential-logic/
├─ 04-machine-language/
├─ 05-cpu/
└─ 06-computer/
```

Each folder includes:
- `.hdl` hardware designs
- `.tst` / `.cmp` test files and results
- Notes & reflections

## 🚀 Next Steps (Coming Soon…)

- Chapter 7: **Assembler**
- Chapter 8–11: **VM + Compiler**
- Chapter 12: **Operating System**

If you're also studying Nand2Tetris — feel free to fork, compare, or open discussions!  
Learning is better together 🤝✨
