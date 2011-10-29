import sys

def numberize(s):
    try:
        return int(''.join([str(ord(c)) for c in s]))
    except TypeError:
        return s

def bit_length(i):
    return len(bin(i).lstrip('-0b'))

def mingle(l):
    l = map(numberize, list(reversed(l)))
    x = 0
    for i in range(max(map(bit_length, l))):
        for j in range(len(l)):
            x += ((l[j] & (1 << i)) << ((len(l)-1)*i+j))
    return x

def zindex(l):
    z = []
    for i in range(len(l)):
        z.append(mingle(l[i]))
    return z

def zorder(l):
    keys = [row[0] for row in l]
    return sorted(zip(zindex(keys), l))

if __name__ == '__main__':
    if sys.argv[1] == 'mingle':
        x = mingle(map(int, sys.argv[2:], [2]*len(sys.argv[2:])))
        print bin(x), bit_length(x)
    else:
        l = [
                [1234, 2345, 3456],
                [1234, 2346, 3457],
                [1234, 2346, 3457],
                [1234, 2347, 3457],
                ['foo', 2347, 3457]
        ]

        print zorder(z)

