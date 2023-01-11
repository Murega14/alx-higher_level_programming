#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    append a string at the end of a text file
    return number of characters added"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
