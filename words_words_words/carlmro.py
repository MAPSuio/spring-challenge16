from sys import stdin

lines = stdin.readlines()

code = ""

for i in xrange(10):
    aggregated_value = 0
    for j in xrange(i*1000, (i*1000) + 1000):
         aggregated_value += sum(map(ord, lines[j]))

    code += chr(aggregated_value % 128)

print code

