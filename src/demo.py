#!/bin/env python
import colorful as cf

from kickapoo.terminal import code_formatter
from kickapoo.terminal.colors import Themes
from kickapoo.terminal.controls import progress, spinner, waiter
from kickapoo.terminal.story import ListSymbol, TerminalStoryTeller


def demo() -> None:
    story = TerminalStoryTeller(writing_speed=96, theme=Themes.SOLARIZED_DARK)
    story.header1("Introduction")
    story.paragraph(
        "This is a demo of the terminal functionality. It uses Terminal Story Teller and will execute exampels of termoinal controls and coloring( courousey of pypi colors)."  # noqa
    )

    story.header2("TerminalStoryTeller")
    lines = """Termial Story Teller provides options for headers[1..4], single layer lists, code formatting, colors using themes. This will use the solarized color theme."""  # noqa
    story.paragraph(lines)

    story.header3("Bullet List Example")
    lines = ["List item {}".format(x) for x in range(5)]
    story.list_writer(lines)

    story.header3("Number List Example")
    story.list_writer(lines, symbol=ListSymbol.NUMBERS)

    story.header3("Letter List Example")
    story.list_writer(lines, symbol=ListSymbol.LETTERS)

    story.header3("Code Styling Example [Python]")

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

    story.header2("Terminal Controls")
    story.paragraph(
        "Terminal controls provide feedback on progress. This is helpful for those of use who need some visualization and color in our terminal lives. hmmmm... that sounds like a pun."  # noqa
    )
    story.paragraph("There are currently 3 controls:")

    story.list_writer(
        ["TerminalProgressBar", "TerminalSpinner", "TerminalSymbolWaiter"]
    )
    story.paragraph(
        "Each has thne following common format options, proding control over display:"
    )

    story.list_writer(
        [
            """prefix: str = "[",                - Prefix for Symbol""",
            """suffix: str = "]",                - Suffix for Symbol""",
            "frames: int = 2,                    - frames allow contgrol for hof fast to update the contorl",  # noqa
            "message_color: TerminalColor = None - Set Message Color",
            "symbol_color: TerminalColor = None  - Set Symbol Color",
            """symbol: str = "."                 - Symbol override""",
        ],
        symbol="-",
    )

    story.header3("TerminalProgressBar Demo")
    story.code_format("""counter = 1
total = 1000000
t_spinner = TerminalProgressBar(
    frames=10000, message_color=FontColor.GREEN, symbol_color=FontColor.CYAN
)
counter = 1
for i in range(1000000):
    t_spinner.render("TerminalProgressBar Demo", counter, total)
    counter += 1
t_spinner.exit()
print("Complete")""")

    story.paragraph("Running TerminalProgressBar...", font_color=cf.yellow)

    counter = 1
    total = 1000000
    t_spinner = progress.TerminalProgressBar(
        frames=10000, message_color=cf.green, symbol_color=cf.cyan
    )
    counter = 1
    for i in range(1000000):
        t_spinner.render("TerminalProgressBar Demo", counter, total)
        counter += 1
    t_spinner.exit()
    print("Complete")

    story.paragraph(
        """The full demo can executed as:
python -m kickapoo.terminal.controls.progress
""",
        font_color=cf.green,
    )

    story.header3("TerminalSymbolWaiter Demo")
    story.code_format("""t_symbol = TerminalSpinner(
        frames=10000, message_color=FontColor.GREEN, symbol_color=FontColor.CYAN
    )
    for i in range(1000000):
        t_symbol.render("TerminalSpinner BASIC & Color Demo")
    t_symbol.exit()
    print("Complete")""")

    story.paragraph("Running TerminalSymbolWaiter...", font_color=cf.yellow)

    t_symbol = spinner.TerminalSpinner(
        frames=10000, message_color=cf.green, symbol_color=cf.cyan
    )
    for i in range(1000000):
        t_symbol.render("TerminalSpinner BASIC & Color Demo")
    t_symbol.exit()
    print("Complete")

    story.paragraph(
        """The full demo can executed as:
python -m kickapoo.terminal.controls.spinner
""",
        font_color=cf.green,
    )

    story.header3("TerminalSymbolWaiter Demo", font_color=cf.yellow)
    story.code_format(""" t_spinner = TerminalSymbolWaiter(
        frames=10000, symbol=" ", symbol_color=cf.on_yellow
    )
    for i in range(1000000):
        t_spinner.render("TerminalSymbolWaiter [Yellow Bar] Demo")
    t_spinner.exit()
    print("Complete")""")

    story.paragraph("Running TerminalSymbolWaiter...", font_color=cf.yellow)

    t_spinner = waiter.TerminalSymbolWaiter(
        frames=10000, symbol=" ", symbol_color=cf.on_yellow
    )
    for i in range(1000000):
        t_spinner.render("TerminalSymbolWaiter [Yellow Bar] Demo")
    t_spinner.exit()
    print("Complete")

    story.paragraph(
        """The full demo can executed as:
python -m kickapoo.terminal.controls.waiter
""",
        font_color=cf.green,
    )

    story.header2("End of Demo")
    story.paragraph(
        """That concludes the demo. Hopefully the contorls are useful for you or inspired you to create your own terminal controls!"""  # noqa
    )


if __name__ == "__main__":
    demo()
