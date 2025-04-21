import enum
import time
from typing import List

from colorful.core import Colorful

from kickapoo.terminal import code_formatter
from kickapoo.terminal.colors import FontFormat, Themes, set_theme


class ListSymbol(enum.StrEnum):
    NUMBERS = "1"
    LETTERS = "A"
    BULLETS = "*"


class TerminalStoryTeller:
    def __init__(self, writing_speed: int = 100, theme: str = Themes.DEFAULT) -> None:
        self._writing_speed = writing_speed
        set_theme(theme)

    def _write(
        self, message: str, font_color: Colorful.ColorfulStyle, line_max: int
    ) -> None:
        if font_color:
            print(font_color)

        line_counter = 1
        line = ""
        for char in message:
            line += char
            if char == "\n":
                print(" ")
                line = ""
                continue
            print(f"\r{line}", end=" ")
            if line_counter % line_max == 0:
                print(" ")
                line = ""
            line_counter += 1
            if self._writing_speed < 100:
                time.sleep((1000 - self._writing_speed * 10) / 1000)

        if font_color:
            print(FontFormat.RESET)

    def header1(self, header: str, font_color: Colorful.ColorfulStyle = None) -> None:
        print(f"{FontFormat.BOLD}{header}{FontFormat.RESET}")

    def header2(self, header: str, font_color: Colorful.ColorfulStyle = None) -> None:
        print(f"{FontFormat.BOLD}{FontFormat.ITALICS}{header}{FontFormat.RESET}")

    def header3(self, header: str, font_color: Colorful.ColorfulStyle = None) -> None:
        print(f"{FontFormat.UNDERLINE}{header}{FontFormat.RESET}")

    def header4(self, header: str, font_color: Colorful.ColorfulStyle = None) -> None:
        print(f"{FontFormat.ITALICS}{header}{FontFormat.RESET}")

    def paragraph(
        self,
        message: str,
        font_color: Colorful.ColorfulStyle = None,
        line_max: int = 88,
    ) -> None:
        self._write(message, font_color, line_max=line_max)
        print("\n")

    def list_writer(
        self,
        items: List[str],
        symbol: ListSymbol = ListSymbol.BULLETS,
        font_color: Colorful.ColorfulStyle = None,
        line_max: int = 88,
    ) -> None:
        current_symbol_value = symbol
        symbol_suffix = (
            "" if symbol not in [ListSymbol.NUMBERS, ListSymbol.LETTERS] else "."
        )
        for item in items:
            self._write(
                f"{current_symbol_value}{symbol_suffix} {item}\n", font_color, line_max
            )
            if symbol == ListSymbol.NUMBERS:
                current_symbol_value = int(current_symbol_value) + 1
            elif symbol == ListSymbol.LETTERS:
                current_symbol_value = chr(ord(current_symbol_value) + 1)

        print("\n")

    def code_format(
        self,
        code: str,
        code_type: code_formatter.CodeType = code_formatter.CodeType.PYTHON,
    ) -> None:
        code_formatter.format_code(code, code_type=code_type)


if __name__ == "__main__":
    # print(type(cf.red), cf.red)
    # raise SystemError

    story = TerminalStoryTeller(writing_speed=98, theme=Themes.SOLARIZED_DARK)
    story.header1("Chapter 1")
    story.paragraph(
        "The vibrant city of Los Angeles, California, is a melting pot of cultures, offering a diverse array of experiences. From the iconic Hollywood Walk of Fame to the stunning beaches of Santa Monica, there's something for everyone. Exploring the city's many neighborhoods, like the trendy shops of Abbot Kinney Boulevard or the art galleries of the Arts District, reveals a unique and dynamic atmosphere."  # noqa
    )

    story.header2("Chapter 2")
    lines = """The vibrant city of Los Angeles, 
California, is a melting pot of cultures, offering a diverse array of experiences. 
From the iconic Hollywood Walk of Fame to the stunning beaches of Santa Monica, 
there's something for everyone. Exploring the city's many neighborhoods, 
like the trendy shops of Abbot Kinney Boulevard or the art galleries of the Arts District, 
reveals a unique and dynamic atmosphere."""  # noqa
    story.paragraph(lines)

    story.header3("Chapter 3 - Bullet List")
    story.list_writer(lines.split("\n"))

    story.header3("Chapter 4 - Number List")
    story.list_writer(lines.split("\n"), symbol=ListSymbol.NUMBERS)

    story.header3("Chapter 5 - Letter List")
    story.list_writer(lines.split("\n"), symbol=ListSymbol.LETTERS)

    code_example = """
def hello_world():
    # This is a comment
    message = "Hello, World!"
    print(message)
    return 42

class MyClass:
    def __init__(self, name):
        self.name = name
        
t_spinner = TerminalSymbolWaiter(frames=10000)
for i in range(1000000):
    t_spinner.render("TerminalSymbolWaiter [Dots] Demo")
    t_spinner.exit()
print("Complete")
"""

    story.code_format(code_example, code_formatter.CodeType.PYTHON)
