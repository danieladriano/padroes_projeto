from commands.command import Command
from commands.no_command import NoCommand


class RemoteControl():
    _on_commands: Command = []
    _off_commands: Command = []

    def __init__(self):
        no_command = NoCommand()
        for i in range(7):
            self._on_commands.append(no_command)
            self._off_commands.append(no_command)

    def set_command(self, slot: int, on_command: Command, off_command: Command):
        self._on_commands[slot] = on_command
        self._off_commands[slot] = off_command

    def on_button_was_pushed(self, slot: int):
        self._on_commands[slot].execute()

    def off_button_was_pushed(self, slot: int):
        self._off_commands[slot].execute()
