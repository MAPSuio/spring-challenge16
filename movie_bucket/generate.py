from random import choice

movies_fd = open('movies.txt', 'ro')
movies = set(map(lambda movie: movie.strip(), movies_fd.readlines()))
movies_fd.close()

inventory = set()

actions = ["buys", "sells", "watches"]

entries = []

entries.append("buys Gone with the Wind")
inventory.add("Gone with the Wind")

while len(entries) < 10000:

    action = choice(actions)

    if action == "buys":
        alternatives = movies.difference(inventory)

        if len(alternatives) == 0:
            continue

        movie = choice(list(alternatives))
        entries.append("buys" + " " + movie)
        inventory.add(movie)
        continue

    if action == "sells":

        alternatives = inventory.difference(set(["Gone with the Wind"]))

        if len(alternatives) == 0:
            continue

        movie = choice(list(alternatives))
        entries.append("sells" + " " + movie)
        inventory.remove(movie)
        continue

    if action == "watches":
        movie = choice(list(inventory))
        entries.append("watches" + " " + movie)

for entry in entries:
    print entry
