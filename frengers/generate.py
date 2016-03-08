from random import choice, shuffle

names_fd = open('names.txt', 'ro')

names = map(lambda name: name.strip(), names_fd.readlines())

events = ["meet", "friends"]

names_fd.close()

entries = set()

while len(entries) < 1000:

    event = choice(events)

    person_a = choice(names)

    person_b = choice(names)

    if person_a == person_b:
        continue

    case = event + " " + person_a + " " + person_b


    if case not in entries:

        equivalent = event + " " + person_b + " " + person_a

        if equivalent not in entries:
            entries.add(case)

result = list(entries)

shuffle(result)

for entry in result:
    print entry
