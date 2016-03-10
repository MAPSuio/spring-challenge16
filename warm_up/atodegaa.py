#There are two very straightforward solutions.
#The first uses the built-in square root, the other simply iterates.
#Both methods are fine in this case, but for bigger numbers the first solution becomes imprecise, and the second method becomes slow.
#In such cases, an implementation of the integer square root algorithm might come in handy. (https://en.wikipedia.org/wiki/Integer_square_root)

#Solution 1
print int(ceil(1234567890**0.5))

#Solution 2
n = 0
while n**2 <= 1234567890:
    n += 1
print n
