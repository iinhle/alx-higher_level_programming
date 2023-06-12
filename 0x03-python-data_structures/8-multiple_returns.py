#!/usr/bin/python3
# 8-multiple_returns.py

def multiple_returns(sentence):
    """returns the len of a strng and its first character."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
