def bitToInt(a):
    if a == 0: return 0 
    a_bit = '{0:b}'.format(a)
    b = ''
    for i in a_bit:
        if i == '0':
            b += '1'
        else:
            b += '0'
    return int(b,2)

assert bitToInt(5) == 2
assert bitToInt(0) == 0
assert bitToInt(1) == 0
assert bitToInt(2) == 1
assert bitToInt(8) == 7
assert bitToInt(16) == 15
