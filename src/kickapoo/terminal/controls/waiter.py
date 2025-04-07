import os
import colorful as cf
from colorful.core import Colorful
from kickapoo.terminal.colors import FontFormat


class TerminalSymbolWaiter:
    def __init__(
        self,
        max: int = -1,
        prefix: str = "",
        suffix: str = "",
        frames: int = 2,
        message_color: Colorful.ColorfulStyle = None,
        symbol_color: Colorful.ColorfulStyle = None,
        symbol: str = ".",
    ) -> None:
        self._spinner = None
        columns, _ = os.get_terminal_size()
        self._max_dots = (
            max if max != -1 else (columns - len(prefix) - len(suffix)) * 0.75
        )  # Arbotraty weight
        self._frames = frames
        self._frame_counter = 0
        self._dots = 0
        self._prefix = prefix
        self._suffix = suffix
        self._message_color = message_color
        self._symbol_color = symbol_color
        self._symbol = symbol

    def make_symbol(self) -> str:
        self._frame_counter += 1
        if self._max_dots < self._dots:
            self._frame_counter = 0
            self._dots = 0

        if self._frame_counter == self._frames or self._spinner is None:
            self._dots += 1
            self._spinner = self._symbol * (self._dots)
            self._frame_counter = 0

        return self._spinner

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
    t_spinner = TerminalSymbolWaiter(frames=10000)
    for i in range(1000000):
        t_spinner.render("TerminalSymbolWaiter [Dots] Demo")
    t_spinner.exit()
    print("Complete")

    t_spinner = TerminalSymbolWaiter(
        frames=10000, message_color=cf.green, symbol_color=cf.cyan
    )
    for i in range(1000000):
        t_spinner.render("TerminalSymbolWaiter [Green and Cyan Text] Demo")
    t_spinner.exit()
    print("Complete")

    t_spinner = TerminalSymbolWaiter(
        frames=10000, symbol=" ", symbol_color=cf.on_yellow
    )
    for i in range(1000000):
        t_spinner.render("TerminalSymbolWaiter [Yellow Bar] Demo")
    t_spinner.exit()
    print("Complete")
