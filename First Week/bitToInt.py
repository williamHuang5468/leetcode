def turnB(a):
    if a == 0:
        return 0 
    a_bit = '{0:b}'.format(a)
    b = ''
    for i in a_bit:
        if i == '0':
            b += '1'
        else:
            b += '0'
    return int(b,2)

assert turnB(5) == 2
assert turnB(0) == 0
assert turnB(1) == 0
assert turnB(2) == 1
assert turnB(8) == 7
assert turnB(16) == 15
