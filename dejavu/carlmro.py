from sys import stdin

pitches = stdin.readlines()

unique_pitches = set(pitches)

print len(pitches) - len(unique_pitches)
