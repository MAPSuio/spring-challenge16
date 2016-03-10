#!/usr/bin/env python

from sys import stdin

def check(line):
    depth = 0

    for c in line:
        if c == "(":
            depth += 1
        if c == ")":
            depth -= 1

            if depth < 0:
                return False

    return depth == 0

def main():
    print(sum(check(line.strip()) for line in stdin))

if __name__ == '__main__':
    main()
