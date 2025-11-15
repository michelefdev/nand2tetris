"""Parser for Hack assembly (A and C commands only).

Follows the nand2tetris Parser API from the book.
"""

class Parser:
    A_COMMAND = "A_COMMAND"
    C_COMMAND = "C_COMMAND"

    def __init__(self, input_file: str):
        with open(input_file, 'r') as f:
            raw = f.readlines()

        self.commands = []
        for line in raw:
            # remove comments
            if '//' in line:
                line = line.split('//', 1)[0]
            line = line.strip()
            if line:
                self.commands.append(line)

        self._current = -1
        self._current_command = None

    def has_more_commands(self) -> bool:
        return self._current + 1 < len(self.commands)

    def advance(self) -> None:
        if not self.has_more_commands():
            raise StopIteration
        self._current += 1
        self._current_command = self.commands[self._current]

    def command_type(self) -> str:
        if self._current_command is None:
            raise RuntimeError("No current command. Call advance() first.")
        if self._current_command.startswith('@'):
            return self.A_COMMAND
        return self.C_COMMAND

    def symbol(self) -> str:
        if self.command_type() != self.A_COMMAND:
            raise RuntimeError("symbol() only valid for A_COMMAND")
        return self._current_command[1:]

    def dest(self) -> str:
        if self.command_type() != self.C_COMMAND:
            raise RuntimeError("dest() only valid for C_COMMAND")
        if '=' in self._current_command:
            return self._current_command.split('=', 1)[0].strip()
        return ''

    def comp(self) -> str:
        if self.command_type() != self.C_COMMAND:
            raise RuntimeError("comp() only valid for C_COMMAND")
        cmd = self._current_command
        # remove dest
        if '=' in cmd:
            _, cmd = cmd.split('=', 1)
        # remove jump
        if ';' in cmd:
            cmd, _ = cmd.split(';', 1)
        return cmd.strip()

    def jump(self) -> str:
        if self.command_type() != self.C_COMMAND:
            raise RuntimeError("jump() only valid for C_COMMAND")
        if ';' in self._current_command:
            return self._current_command.split(';', 1)[1].strip()
        return ''
