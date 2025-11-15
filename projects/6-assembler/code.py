"""Code module: translate Hack mnemonics to binary codes.

Provides dest, comp, and jump translation methods matching the book.
"""

class Code:
    def __init__(self):
        self._dest = {
            '': '000',
            'M': '001',
            'D': '010',
            'MD': '011',
            'A': '100',
            'AM': '101',
            'AD': '110',
            'AMD': '111',
        }

        self._jump = {
            '': '000',
            'JGT': '001',
            'JEQ': '010',
            'JGE': '011',
            'JLT': '100',
            'JNE': '101',
            'JLE': '110',
            'JMP': '111',
        }

        # comp -> 7 bits (a c1..c6)
        self._comp = {
            # a = 0 (uses A)
            '0':   '0101010',
            '1':   '0111111',
            '-1':  '0111010',
            'D':   '0001100',
            'A':   '0110000',
            '!D':  '0001101',
            '!A':  '0110001',
            '-D':  '0001111',
            '-A':  '0110011',
            'D+1': '0011111',
            'A+1': '0110111',
            'D-1': '0001110',
            'A-1': '0110010',
            'D+A': '0000010',
            'D-A': '0010011',
            'A-D': '0000111',
            'D&A': '0000000',
            'D|A': '0010101',
            # a = 1 (uses M)
            'M':   '1110000',
            '!M':  '1110001',
            '-M':  '1110011',
            'M+1': '1110111',
            'M-1': '1110010',
            'D+M': '1000010',
            'D-M': '1010011',
            'M-D': '1000111',
            'D&M': '1000000',
            'D|M': '1010101',
        }

    def dest(self, mnemonic: str) -> str:
        return self._dest.get(mnemonic, '000')

    def comp(self, mnemonic: str) -> str:
        if mnemonic not in self._comp:
            raise KeyError(f"Unknown comp mnemonic: {mnemonic}")
        return self._comp[mnemonic]

    def jump(self, mnemonic: str) -> str:
        return self._jump.get(mnemonic, '000')
