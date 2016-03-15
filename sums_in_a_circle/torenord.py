#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solutions(lst):
    N = len(lst)

    # Hvis alle firkanter er fylt inn:
    if 0 not in lst[::2]:
        # Det er én sirkel igjen, helt til høyre i listen.
        m = N-1

        # Test om vi får en gyldig løsningen ved å fylle inn den
        # siste.
        y = lst[m-1] + lst[m+1-N]
        if y not in lst and y < N:
            lst[m] = y
            return [lst]

        # Hvis ikke, returner tomt.
        else:
            return []

    # Indeks til første tomme firkant.
    m = 2*lst[::2].index(0)

    ret = []

    # Vi bruker tallene vi har igjen og tester ut hva som blir
    # neste firkant.
    for x in [x for x in range(1, N) if x not in lst]:
        y = x + lst[m-2]

        if y not in lst and y < N:
            # Her har vi en potensiell vinner, så vi lager en ny
            # liste, setter inn tallet i firkanten, regner ut sirkelen
            # til venstre og gjør et rekursivt kall som fortsetter
            # arbeidet.

            new_lst = list(lst)
            new_lst[m] = x
            new_lst[m-1] = y

            # Samler opp løsningene vi har funnet.
            ret += solutions(new_lst)

    return ret

def solve(N):
    # Det finnes ingen løsninger hvis N er et oddetall.
    if N % 2 == 1:
        return 0

    # Hvis N = 2, er 2 i en sirkel og 1 i firkanten til venstre og
    # høyre for 2 siden de er koblet i en loop.
    if N == 2:
        return 1

    # Antall løsninger.
    count = 0

    # Vi kan begynne på 2 fordi N-1 må være i en sirkel.
    for i in range(2, N//2):
        for solution in solutions([N-i, N, i] + [0]*(N-3)):
            count += 1

    return count

if __name__ == '__main__':
    print solve(20)
