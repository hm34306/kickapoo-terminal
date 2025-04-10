from typing import ClassVar, List

import colorful as cf
from colorful.core import Colorful

from kickapoo.terminal.colors import FontFormat


class SpinnerType:
    BASIC: ClassVar[List[str]] = ["\\", "|", "/", "-", "\\", "|", "/", "*"]
    DOTS: ClassVar[List[str]] = [".", "..", "...", "....", ".....", "......"]
    SPECIAL: ClassVar[List[str]] = ["!", "@", "#", "$", "%", "^", "&", "-", "+"]


class TerminalSpinner:
    def __init__(
        self,
        spinner_list: List[str] = SpinnerType.BASIC,
        prefix: str = "",
        suffix: str = "",
        frames: int = 2,
        message_color: Colorful.ColorfulStyle = None,
        symbol_color: Colorful.ColorfulStyle = None,
    ) -> None:
        self._symbol = None
        self._symbol_list = spinner_list
        self._frames = frames
        self._frame_counter = 0
        self._counter = 0
        self._prefix = prefix
        self._suffix = suffix
        self._message_color = message_color
        self._symbol_color = symbol_color

    def make_symbol(self) -> List[str]:
        self._counter += 1
        self._frame_counter += 1
        if self._frames < self._frame_counter:
            self._frame_counter = 0

        if self._frame_counter == self._frames or self._symbol is None:
            index = (self._counter % len(self._symbol_list)) - 1
            self._symbol = self._symbol_list[index]

        return self._symbol

    def get_symbol(self, message: str) -> str:
        spin = self.make_symbol()
        if self._symbol_color is not None:
            spin = f"{self._symbol_color}{spin}{FontFormat.RESET}"
        if self._message_color is not None:
            message = f"{self._message_color}{message}{FontFormat.RESET}"
        return f"\r{message} {self._prefix}{spin} {self._suffix}"

    def render(self, message: str) -> None:
        print(self.get_symbol(message), end="")

    def exit(self) -> None:
        print("")


if __name__ == "__main__":
    t_symbol = TerminalSpinner(frames=10000)
    for i in range(1000000):
        t_symbol.render("TerminalSpinner BASIC Demo")
    t_symbol.exit()
    print("Complete")

    t_symbol = TerminalSpinner(
        frames=10000, message_color=cf.green, symbol_color=cf.cyan
    )
    for i in range(1000000):
        t_symbol.render("TerminalSpinner BASIC & Color Demo")
    t_symbol.exit()
    print("Complete")

    t_symbol = TerminalSpinner(spinner_list=SpinnerType.DOTS, frames=10000)
    print("Spinner Demo: ")
    for i in range(1000000):
        t_symbol.render("TerminalSpinner DOTS Demo")
    t_symbol.exit()
    print("Complete")

    t_symbol = TerminalSpinner(spinner_list=SpinnerType.SPECIAL, frames=100000)
    print("Spinner Test")
    for i in range(1000000):
        t_symbol.render("TerminalSpinner SPECIAL Demo")
    t_symbol.exit()
    print("Complete")
