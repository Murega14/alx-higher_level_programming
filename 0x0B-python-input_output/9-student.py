#!/usr/bin/python3
"""Defines a class student."""

class Student:
    """Represents a student."""
    def __init__(self, first_name, last_name, age):
        """Initializes a new student.
        Args:
            first_name(str): Students first name.
            last_name(str): Students last name.
            age(int): students age"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the student."""
        return self.__dict__
