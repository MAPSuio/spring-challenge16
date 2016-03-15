#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import stdin
from base64 import b64decode

# Fra https://en.wikipedia.org/wiki/Portable_Network_Graphics
magic_number = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]

# Leser filen fra standard in
content = b64decode(stdin.read())

# Xor'er de første 8 tegnene med magic_number
decoded = "".join(chr(ord(content[i]) ^ magic_number[i]) for i in range(len(magic_number)))

# Vi ser på decoded at nøkkelen er 5 tegn lang:
print decoded[:5]
