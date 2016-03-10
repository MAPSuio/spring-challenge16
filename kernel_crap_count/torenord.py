#!/usr/bin/env python

import os
import sys

def solve(path):
    count = 0

    for root, _, files in os.walk(path):
        for filename in files:
            with open(os.path.join(root, filename)) as f:
                for line in f:
                    count += line.lower().count("crap")

    return count

def main():
    if len(sys.argv) != 2:
        print("Usage: python %s path" % sys.argv[0])
    else:
        print(solve(sys.argv[1]))

if __name__ == '__main__':
    main()
