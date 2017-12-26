from math import factorial


def nth_perm(pos, L):
    pos -= 1
    perm = []
    for i in reversed(range(len(L))):
        c = pos//factorial(i)
        perm.append(L[c])
        L.remove(L[c])
        pos -= c*factorial(i)
    return perm

print("".join([str(x) for x in nth_perm(1000000, [x for x in range(10)])]))
