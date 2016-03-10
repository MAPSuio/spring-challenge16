#Simply multiplying and comparing against the given number is not efficient enough to solve this problem. (At least, so we think, we haven't checked fully).
#The idea is to use logarithms to transform everything into sums rather than multiplications, and make the numbers much smaller.
#The given starting values are in fact 2^26 and 2^47, so base 2 seems like a sensible choice.

#Define a new sequence G_n = log_2(F_n). Then the question becomes to find the smallest k such that G_k >= 74207281.
#However, G kan be defined as G_0 = log_2(F_0) = 26, G_1 = log_2(F_1) = 47, G_n = log_2(F_(n-1)F_(n-2)) = log_2(F_(n-1)) + log_2(F_(n-2)) = G_(n-1) + G_(n-2).
#This is a straightforward Fibonacci problem. Here's some code which gives the answer:

mem = {0: 26, 1: 47}

def G(n):
    if n in mem:
        return mem[n]
    else:
        tmp = G(n-1) + G(n-2)
        mem[n] = tmp
        return tmp

i = 0
while G(i) < 74207281:
    i += 1
print i
