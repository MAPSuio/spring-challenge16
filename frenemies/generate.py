from random import choice, shuffle

names_fd = open('names.txt', 'ro')

names = map(lambda name: name.strip(), names_fd.readlines())

names_fd.close()

events = []

for i in xrange(3):
    events.append("friends")

events.append("hates")

entries = set()

while len(entries) < 20000:

    event = choice(events)

    person_a = choice(names)

    person_b = choice(names)

    case = ""

    if event == "hates":
        case = person_a + " hates " + person_b
    else:
        case = "friends " + person_a + " " + person_b

    entries.add(case)

result = list(entries)

shuffle(result)

for entry in result:
    print entry
