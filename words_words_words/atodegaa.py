words = []
infile = open("data.txt", "r")
for line in infile:
    words.append(line)

final = ""
for i in xrange(10):
    ascii_sum = 0
    for j in xrange(i*1000, (i+1)*1000):
        ascii_sum += sum(ord(c) for c in words[j])
    final += chr(ascii_sum % 128)
print final
