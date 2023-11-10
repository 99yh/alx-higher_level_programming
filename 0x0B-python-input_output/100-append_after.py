#!/usr/bin/python3
"""Module to search for somthing in a file and update that file."""


def append_after(filename="", search_string="", new_string=""):
    """
    Add ``new_string`` after any line containing ``search_string``
    in the given ``filename``
    """
    lines = []
    if search_string and new_string:
        with open(filename, "r") as f:
            for line in f:
                lines.append(line)
                if search_string in line:
                    lines.append(new_string)
    if lines:
        with open(filename, "w") as f:
            f.writelines(lines)
