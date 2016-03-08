
data_fd = open('data.txt', 'ro')
entries = map(lambda entries: entries.strip(), data_fd.readlines())
data_fd.close()

friend_map = {}
meet_map = {}

frengers = set()

for entry in entries:
    event, person_a, person_b = entry.split()

    if event == "friends":

        if person_a not in friend_map:
            friend_map[person_a] = set()
        friend_map[person_a].add(person_b)

        if person_b not in friend_map:
            friend_map[person_b] = set()
        friend_map[person_b].add(person_a)

    if event == "meet":

        if person_a not in meet_map:
            meet_map[person_a] = set()
        meet_map[person_a].add(person_b)

        if person_b not in meet_map:
            meet_map[person_b] = set()
        meet_map[person_b].add(person_a)

for person in friend_map:

    possible_frengers = meet_map[person].difference(friend_map[person])

    for possible_frenger in possible_frengers:

        friends_in_common = friend_map[person].intersection(friend_map[possible_frenger])

        if len(friends_in_common) >= 3:

            if (person, possible_frenger) not in frengers and (possible_frenger, person) not in frengers:
                frengers.add((person, possible_frenger))

print len(frengers)
