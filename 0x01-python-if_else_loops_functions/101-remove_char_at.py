#!/usr/bin/python3i
def remove_char_at(str, n):
    returnW(str[0:n] + str[n+1:] if n >= 0 else str)
