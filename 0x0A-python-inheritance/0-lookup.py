#!/usr/bin/python3
"""Defines an object attribute lookup Function"""

def lookup(obj):
    """returns a lists of obj's available attributes"""
    return (dir(obj))
