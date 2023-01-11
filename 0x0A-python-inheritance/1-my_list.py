#!/usr/bin/python3
"""class mylist"""


class MyList(list):
    """prints class' sorted list"""
    def print_sorted(self):
        print(sorted(self)):
