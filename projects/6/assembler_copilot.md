# copilot: enable
# Project: Hack Assembler (No Symbols)
This project implements the Hack Assembler exactly as described in the *Nand2Tetris* book (chapters 6).  
It should translate `.asm` files into `.hack` binary files.  
This assembler **does not** implement symbol resolution (no labels, no variables).

The assembler must contain at minimum:
- A **Parser** module
- A **Code** module
- A main driver that uses both

The implementation should follow the architecture and API definitions from the book.

---

# Coding Style Expectations
- Use simple, clean, idiomatic Python.
- Keep modules small and pure; avoid global state.
- Use classes only where required by the Nand2Tetris API design.
- Do not use external libraries.
- Keep methods very close to the textbook specification.

---

# Parser Module Specification
## File: `parser.py`
Class: `Parser`

### Purpose
Reads an `.asm` file and provides access to its assembly instructions.

### Behavior
- Removes whitespace and comments.
- Provides instruction-by-instruction iteration.
- Only handles **A-instructions** and **C-instructions** (no labels or variables).

### API (as defined in the book)

```python
class Parser:
    def __init__(self, input_file): ...
    def has_more_commands(self) -> bool: ...
    def advance(self) -> None: ...
    def command_type(self) -> str: ... 
        # returns "A_COMMAND" or "C_COMMAND"
    def symbol(self) -> str: ...
        # only valid for A_COMMAND, return string after '@'
    def dest(self) -> str: ...
        # returns dest mnemonic or '' if none
    def comp(self) -> str: ...
    def jump(self) -> str: ...

```

# Code Module Specification
## File: code.py
Class: `Code`

### Responsibilities
Translate Hack mnemonics into binary codes.

### API (must match the Nand2Tetris spec)

- `dest(mnemonic: str) -> str`  
  Returns 3-bit dest binary code.
- `comp(mnemonic: str) -> str`  
  Returns 7-bit comp binary code.
- `jump(mnemonic: str) -> str`  
  Returns 3-bit jump binary code.

Must include the full set of Hack CPU mnemonics and match exactly the ones in the book.

---

# Main Assembler Module
## File: assembler.py

Responsibilities:
1. Open input `.asm`
2. Create `Parser`
3. Create `Code`
4. For each command:
   - If A-instruction: output `0vvvvvvvvvvvvvvv`
   - If C-instruction: output  
     `111` + comp bits + dest bits + jump bits
5. Write each result line to `.hack` output file.

---

# Constraints
- **No symbol table**
- **No first or second pass**
- **No label declarations**
- **No variable allocation**
- Input contains only A and C instructions.

---

# Copilot Guidance
### Copilot should prioritize:
- Clean, small, accurate functions
- Staying as close to the Nand2Tetris canonical design as possible
- Minimal abstractions
- Deterministic, testable output

### Copilot should avoid:
- Adding extra language features
- Adding new mnemonics
- Implementing labels or symbols
- Over-engineering the parser or code module
