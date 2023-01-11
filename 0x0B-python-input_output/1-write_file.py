#!/usr/bin/python3
"""returns number of lines"""


def write_file(filename="", text=""):
    """number of lines"""
    lines = 0
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            lines += 1
    return lines
    
