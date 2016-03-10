def minedges(n):
    i = int(n**0.5)
    while i > 1:
        if n % i == 0:
            break
        i -= 1
    return (i, n/i)

def edgepieces((n,m)):
    if n == 1:
        return m
    return 2*n + 2*m - 4

print edgepieces(minedges(8387035452956160000))
