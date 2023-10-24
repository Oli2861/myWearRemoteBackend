import os
from abc import ABC, abstractmethod
from enum import Enum

import win32api


class Command(Enum):
    PLAY = 0
    PAUSE = 1
    NEXT = 2
    PREVIOUS = 3
    VOLUME_UP = 4
    VOLUME_DOWN = 5
    LEFT = 6
    RIGHT = 7
    UP = 8
    DOWN = 9
    SELECT = 10


class CommandExecutor(ABC):
    @abstractmethod
    def execute(self, command: Command):
        pass


class WindowsCommandExecutor(CommandExecutor):

    def __init__(self):
        self.command_map = {
            Command.PLAY: 0xB3,
            Command.PAUSE: 0xB3,
            Command.NEXT: 0xB0,
            Command.PREVIOUS: 0xB1,
            Command.VOLUME_UP: 0xAF,
            Command.VOLUME_DOWN: 0xAE,
            Command.LEFT: 0x25,
            Command.RIGHT: 0x27,
            Command.UP: 0x26,
            Command.DOWN: 0x28,
            Command.SELECT: 0x0D
        }

    def execute(self, command: Command) -> bool:
        """
        :param command: The command to execute.
        :return: Whether the command was executed successfully.
        """
        if command in self.command_map:
            # Press & release key
            win32api.keybd_event(self.command_map[command], 0, 0, 0)
            win32api.keybd_event(self.command_map[command], 0, 2, 0)
            print(f"Executed command {command}")
            return True
        else:
            print(f"Command {command} not found")
            return False


command_provider: CommandExecutor | None = None
if os.name == "nt":
    command_provider = WindowsCommandExecutor()


def get_command_provider() -> CommandExecutor:
    assert command_provider is not None
    return command_provider
