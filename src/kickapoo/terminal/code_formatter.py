import re
from enum import Enum

import colorful as cf

from kickapoo.terminal.colors import FontFormat
from kickapoo.terminal.symbols import Symbols


class CodeType(Enum):
    PYTHON = "python"
    JAVASCRIPT = "javascript"
    HTML = "html"
    CSS = "css"


def format_code(code: str, code_type: CodeType = CodeType.PYTHON) -> None:
    """Format and print code with syntax highlighting using colorful"""
    print(
        f"{cf.yellow}<--- BEGIN {Symbols.PYTHON} {cf.magenta}<{code_type}>{cf.yellow} Code Block --->{FontFormat.RESET}"  # noqa
    )

    if code_type == CodeType.PYTHON:
        # Process the code line by line
        lines = code.split("\n")
        for line in lines:
            # Extract indentation
            indent_match = re.match(r"^(\s+)", line)
            indent = indent_match.group(1) if indent_match else ""
            line_without_indent = line.lstrip()

            # Handle comment lines
            if line_without_indent.startswith("#"):
                print(f"{indent}{cf.green(line_without_indent)}")
                continue

            # Process the line character by character for maximum control
            i = 0
            output = []

            while i < len(line_without_indent):
                # Check for strings
                if i < len(line_without_indent) and line_without_indent[i] in [
                    "'",
                    '"',
                ]:
                    # Found a string
                    quote = line_without_indent[i]
                    j = i + 1
                    while j < len(line_without_indent):
                        if (
                            line_without_indent[j] == quote
                            and line_without_indent[j - 1] != "\\"
                        ):
                            break
                        j += 1

                    if j < len(line_without_indent):
                        j += 1  # Include the closing quote

                    string_content = line_without_indent[i:j]
                    output.append(cf.green(string_content))
                    i = j
                    continue

                # Check for keywords
                keywords = [
                    "def",
                    "class",
                    "import",
                    "from",
                    "for",
                    "in",
                    "if",
                    "else",
                    "elif",
                    "while",
                    "return",
                    "True",
                    "False",
                    "None",
                    "and",
                    "or",
                    "not",
                    "try",
                    "except",
                    "finally",
                    "with",
                    "as",
                    "break",
                    "continue",
                    "pass",
                    "raise",
                    "assert",
                    "is",
                    "lambda",
                    "yield",
                ]

                # Extract a word if we're at the beginning of one
                if i < len(line_without_indent) and (
                    line_without_indent[i].isalpha() or line_without_indent[i] == "_"
                ):
                    j = i + 1
                    while j < len(line_without_indent) and (
                        line_without_indent[j].isalnum()
                        or line_without_indent[j] == "_"
                    ):
                        j += 1

                    word = line_without_indent[i:j]

                    # Color based on what the word is
                    if word in keywords:
                        output.append(cf.magenta(word))
                    elif word == "self":
                        output.append(cf.yellow(word))
                    else:
                        # Check if it's a function call (followed by open parenthesis)
                        is_function = False
                        for k in range(j, len(line_without_indent)):
                            if line_without_indent[k].isspace():
                                continue
                            if line_without_indent[k] == "(":
                                is_function = True
                            break

                        if is_function:
                            output.append(cf.cyan(word))
                        else:
                            output.append(word)

                    i = j
                    continue

                # Check for numbers
                if i < len(line_without_indent) and line_without_indent[i].isdigit():
                    j = i + 1
                    while j < len(line_without_indent) and (
                        line_without_indent[j].isdigit()
                        or line_without_indent[j] == "."
                    ):
                        j += 1

                    number = line_without_indent[i:j]
                    output.append(cf.blue(number))
                    i = j
                    continue

                # Regular character
                if i < len(line_without_indent):
                    output.append(line_without_indent[i])
                    i += 1

            formatted: str = ""
            for s in output:
                formatted += f"{s}"
            # Print the formatted line
            print(f"{indent}{formatted}")

        print(f"{cf.yellow}<--- END Code Block --->{FontFormat.RESET}")
        print("")
