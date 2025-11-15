"""Simple Hack assembler (no symbols).

Usage: python assembler.py input.asm

This assembler implements only numeric A-instructions and C-instructions.
It produces a .hack file with 16-bit binary instructions.
"""

import sys
from pathlib import Path

from code import Code
from parser import Parser


def assemble(input_path: str, output_path: str) -> None:
	parser = Parser(input_path)
	coder = Code()

	out_lines = []
	while parser.has_more_commands():
		parser.advance()
		t = parser.command_type()
		if t == parser.A_COMMAND:
			sym = parser.symbol()
			# this assembler doesn't support symbols; only decimal numbers
			try:
				val = int(sym)
			except ValueError:
				raise ValueError(f"Non-numeric A-instruction symbol encountered: {sym}")
			if val < 0 or val > 32767:
				raise ValueError(f"A-instruction value out of range (0..32767): {val}")
			out_lines.append('0' + format(val, '015b'))
		else:
			comp_bits = coder.comp(parser.comp())
			dest_bits = coder.dest(parser.dest())
			jump_bits = coder.jump(parser.jump())
			out_lines.append('111' + comp_bits + dest_bits + jump_bits)

	with open(output_path, 'w') as f:
		for line in out_lines:
			f.write(line + '\n')


def _default_output_path(in_path: str) -> str:
	p = Path(in_path)
	if p.suffix.lower() == '.asm':
		return str(p.with_suffix('.hack'))
	return str(p) + '.hack'


def main(argv):
	if len(argv) < 2:
		print('Usage: python assembler.py input.asm')
		return 1
	inp = argv[1]
	outp = argv[2] if len(argv) > 2 else _default_output_path(inp)
	assemble(inp, outp)
	return 0


if __name__ == '__main__':
	raise SystemExit(main(sys.argv))

