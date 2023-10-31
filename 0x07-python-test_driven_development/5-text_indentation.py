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
    for c in text:
        line = line + c
        if c in ".?:\n":
            _text = _text + line.lstrip() + '\n' * 2 * (c != '\n')
            line = ""
    print(_text)

Module ``5-text_indentation``
