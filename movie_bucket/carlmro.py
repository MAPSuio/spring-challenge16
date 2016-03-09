from sys import stdin

events = map(lambda line: line.strip(), stdin.readlines())

stack = []

for event in events:

    tokens = event.split()
    action = tokens[0]
    movie = " ".join(tokens[1:])

    if action == "buys":
        stack.append(movie)

    if action == "sells":
        stack.remove(movie)

    if action == "watches":
        stack.remove(movie)
        stack.append(movie)

position = 0
movie = ""

while movie != "Gone with the Wind":
    movie = stack.pop()
    position += 1

print position
