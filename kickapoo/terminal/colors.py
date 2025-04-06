from typing import TypeVar


TerminalColor = TypeVar('TerminalColor')

class _ResetFont():
    RESET: TerminalColor = '\033[0m'

class FontColor(_ResetFont):
    YELLOW: TerminalColor = '\033[91m'
    GREEN: TerminalColor = '\033[92m'
    RED: TerminalColor = '\033[93m'
    BLUE: TerminalColor = '\033[94m'
    MAGENTA: TerminalColor = '\033[95m'
    CYAN: TerminalColor = '\033[96m'
    RESET: TerminalColor = '\033[0m'


class FontFotmat(_ResetFont):
    BOLD: TerminalColor = '\033[1m'
    FAINT: TerminalColor = '\033[2m'
    ITALICS: TerminalColor = '\033[3m'
    UNDERLINE: TerminalColor = '\033[4m'


class BackgroundColor(_ResetFont):
    RED: TerminalColor = '\033[41m'
    GREEN: TerminalColor = '\033[42m'
    YELLOW: TerminalColor = '\033[43m'
    BLUE: TerminalColor = '\033[44m'
    MAGENTA: TerminalColor = '\033[45m'
    CYAN: TerminalColor= '\033[46m'


def green(msg):
    return f"C{FontColor.GREEN}{msg}{FontColor.RESET}"


def yellow(msg):
    return f"C{FontColor.YELLOW}{msg}{FontColor.RESET}"


def red(msg):
    return f"C{FontColor.RED}{msg}{FontColor.RESET}"


def cyan(msg):
    return f"C{FontColor.CYAN}{msg}{FontColor.RESET}"


def magenta(msg):
    return f"C{FontColor.CYAN}{msg}{FontColor.RESET}"
