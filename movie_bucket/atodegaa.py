from sys import stdin
infile = [i.strip() for i in stdin.readlines()]

stack = []

for line in infile:
    if line.startswith("buys"):
        movie = line[5:]
        stack.append(movie)
    elif line.startswith("sells"):
        movie = line[6:]
        stack.remove(movie)
    else:
        movie = line[8:]
        stack.remove(movie)
        stack.append(movie)

print len(stack) - stack.index("Gone with the Wind")
