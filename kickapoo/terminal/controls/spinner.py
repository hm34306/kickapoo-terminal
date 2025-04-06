from typing import List
from kickapoo.terminal.colors import FontColor, TerminalColor


class SpinnerType:
    BASIC = [ "\\", "|", "/", "-", "\\", "|", "/", "*"]
    DOTS = [ ".", "..", "...", "....", ".....", "......"]
    SPECIAL = [ "!", "@", "#", "$", "%", "^", "&", "-", "+"]


class TerminalSpinner():

    def __init__(self, spinner_list: List[str]=SpinnerType.BASIC, prefix: str="", suffix: str="", frames: int=2, message_color: TerminalColor=None, symbol_color: TerminalColor=None):
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
            index = (self._counter % len(self._symbol_list)) -1
            self._symbol = self._symbol_list[index]

        return self._symbol

    def get_symbol(self, message: str) -> str:
        spin = self.make_symbol()
        if self._symbol_color is not None:
            spin = f"{self._symbol_color}{spin}{FontColor.RESET}"
        if self._message_color is not None:
            message = f"{self._message_color}{message}{FontColor.RESET}"
        return f"\r{message} {self._prefix}{spin} {self._suffix}"

    def render(self, message: str) -> None:
        print(self.get_symbol(message), end="")

    def exit(self) -> None:
        print("")

    
if __name__ == "__main__":
    t_symbol = TerminalSpinner(frames=10000)
    for i in range(1000000):
        t_symbol.print("Spinner BASIC Demo")
    t_symbol.exit()
    print("Complete")

    t_symbol = TerminalSpinner(frames=10000, message_color=FontColor.GREEN, symbol_color=FontColor.CYAN)
    for i in range(1000000):
        t_symbol.print("Spinner BASIC Demo")
    t_symbol.exit()
    print("Complete")

    t_symbol = TerminalSpinner(spinner_list=SpinnerType.DOTS,frames=10000)
    print("Spinner Demo: ")
    for i in range(1000000):
        t_symbol.print("Spinner DOTS Demo")
    t_symbol.exit()
    print("Complete")

    t_symbol = TerminalSpinner(spinner_list=SpinnerType.SPECIAL,frames=100000)
    print("Spinner Test")
    for i in range(1000000):
        t_symbol.print("Spinner SPECIAL Demo")
    t_symbol.exit()
    print("Complete")
