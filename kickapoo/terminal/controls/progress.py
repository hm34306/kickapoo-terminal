import os
from kickapoo.terminal.colors import BackgroundColor,  FontColor


class TerminalProgressBar():

    def __init__(self, max=100, prefix="[", suffix="]", frames=2, message_color=None, symbol_color=None, symbol="."):
        self._spinner = None
        columns, _  = os.get_terminal_size()
        self._max_dots = max if max is not None else (columns - len(prefix) - len(suffix) )
        self._frames = frames
        self._frame_counter = 0
        self._dots = 0
        self._prefix = prefix
        self._suffix = suffix
        self._message_color = message_color
        self._symbol_color = symbol_color
        self._symbol = symbol

    def make_symbol(self, progress, total):
        self._frame_counter += 1
        if self._max_dots < self._dots:
            self._frame_counter = 0
            self._dots = 0
        
        if self._frame_counter == self._frames or self._spinner is None:
            self._dots = 1 if progress == 0 else (progress / total) * 100
            self._spinner = self._symbol * (int(self._dots))
            self._frame_counter = 0

        return self._spinner

    def get_symbol(self, message, progress, total):
        spin = self.make_symbol(progress, total)
        if self._symbol_color is not None:
            spin = f"{self._symbol_color}{spin}{FontColor.RESET}"
        if self._message_color is not None:
            message = f"{self._message_color}{message}{FontColor.RESET}"
        percent = int((progress / total) * 100)
        return f"\r{message} {self._prefix}{spin}{self._suffix} {percent}%"

    def render(self, message, progress, total):
        print(self.get_symbol(message, progress, total), end="")

    def exit(self):
        print("")

    
if __name__ == "__main__":
    t_spinner = TerminalProgressBar(frames=10000)
    counter = 1
    total = 1000000
    for i in range(total):
        t_spinner.render("TerminalProgressBar Demo", counter, total)
        counter += 1
    t_spinner.exit()
    print("Complete")

    t_spinner = TerminalProgressBar(frames=10000, message_color=FontColor.GREEN, symbol_color=FontColor.CYAN)
    counter = 1
    for i in range(1000000):
        t_spinner.render("TerminalProgressBar Demo", counter, total)
        counter += 1
    t_spinner.exit()
    print("Complete")

    t_spinner = TerminalProgressBar(frames=10000, symbol=" ", symbol_color=BackgroundColor.YELLOW)
    counter = 1
    for i in range(1000000):
        t_spinner.render("TerminalProgressBar Demo", counter, total)
        counter += 1
    t_spinner.exit()
    print("Complete")
