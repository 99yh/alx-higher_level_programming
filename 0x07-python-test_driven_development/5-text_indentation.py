#!/usr/bin/python3
"""Module for text indentaion."""


def text_indentation(text):
    """
    Print a text with 2 lines after any ., ? and :

    Params
    ------
    text : str
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    _text = ""
    line = ""
    c = '\n'
    for c in text:
        line = line + c
        if c == '\n':
            _text = _text + line.strip() + '\n'
            line = ""
        if c in ".?:":
            _text = _text + line.strip() + '\n' * 2
            line = ""
    if c not in ".?:\n":
        _text = _text + line.strip()
    print(_text, end="")
