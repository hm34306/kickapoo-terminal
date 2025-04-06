import colorful as cf
from enum import StrEnum


class ColorName(StrEnum):
    RED = "red"
    GREEN = "green"
    YELLOW = "yellow"
    BLUE = "blue"
    MAGENTA = "magenta"
    CYAN = "cyan"
    RESET = "reset"


class FontFormat(StrEnum):
    # Raw ANSI codes for terminals that support them
    BOLD = '\033[1m'
    FAINT = '\033[2m'
    ITALICS = '\033[3m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


class Themes(StrEnum):
    DEFAULT = "Default"
    SOLARIZED_DARK = "solarized"
    MONOKAI = "monokai"


class FontFormat(StrEnum):
    # Raw ANSI codes for terminals that support them
    BOLD = '\033[1m'
    FAINT = '\033[2m'
    ITALICS = '\033[3m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


# Create theme management functions
def set_theme(theme_name):
    """Set a color theme by name"""
    try:
        print(theme_name)
        cf.use_style(theme_name)
        return True
    except ValueError:
        #print(f"Theme '{theme_name}' not found. Using default.")
        return False

def get_available_themes():
    """Returns a list of available themes"""
    return list(cf.styles.keys())

# Convenience functions for colored text
def red(text):
    return cf.red(text)

def green(text):
    return cf.green(text)

def yellow(text):
    return cf.yellow(text)

def blue(text):
    return cf.blue(text)

def magenta(text):
    return cf.magenta(text)

def cyan(text):
    return cf.cyan(text)

def bold(text):
    return f"{FontFormat.BOLD}{text}{FontFormat.RESET}"

def italic(text):
    return f"{FontFormat.ITALICS}{text}{FontFormat.RESET}"

def underline(text):
    return f"{FontFormat.UNDERLINE}{text}{FontFormat.RESET}"