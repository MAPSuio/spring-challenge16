#!/usr/bin/env python

from sys import stdin

def check(line):
    stack = []

    lparens = ["(", "[", "{"]
    rparens = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    for c in line:
        if c in lparens:
            stack.append(c)
        if c in rparens:
            if len(stack) == 0 or stack.pop() != rparens[c]:
                return False

    return stack == []

def main():
    print(sum(check(line.strip()) for line in stdin))

if __name__ == '__main__':
    main()
