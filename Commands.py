from abc import ABC, abstractmethod

import win32api


class Commands(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def previous(self):
        pass


class WindowsCommands(Commands):
    def play(self):
        print("Executing play command")
        win32api.keybd_event(0xB3, 0, 0, 0)

    def pause(self):
        print("Executing pause command")
        win32api.keybd_event(0xB3, 0, 0, 0)

    def next(self):
        print("Executing next command")
        win32api.keybd_event(0xB0, 0, 0, 0)

    def previous(self):
        print("Executing previous command")
        win32api.keybd_event(0xB1, 0, 0, 0)
