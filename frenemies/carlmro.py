from sys import stdin

entries = map(lambda line: line.strip(), stdin.readlines())

friends = []
hate_map = {}

for entry in entries:
    words = entry.split()

    if words[0] == "friends":
        friends.append((words[1], words[2]))
    else:
        if words[0] not in hate_map:
            hate_map[words[0]] = set()

        hate_map[words[0]].add(words[2])

frenemies = 0

for pair in friends:
    person_a, person_b = pair

    if (person_b in hate_map[person_a]) and (person_a in hate_map[person_b]):
        frenemies += 1

print frenemies
