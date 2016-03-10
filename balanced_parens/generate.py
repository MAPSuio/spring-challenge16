#!/usr/bin/env python

from random import choice, randint

def generate(depth):
    """Print random looking balanced expression of specified depth"""

    typ = choice(["()"])

    if depth == 0:
        return ""
    if depth == 1:
        return typ

    return choice([lambda _: typ[0] + generate(depth-1) + typ[1],
                   lambda r: generate(r) + generate(depth-r)])(randint(0, depth))

def main():
    for _ in range(50):
        print generate(40)

if __name__ == '__main__':
    main()
