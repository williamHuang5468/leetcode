def hammingDistance(a, b):
    return sum([1 for i in bin(a^b) if i is "1"])

'''
def hammingDistance(a, b):
    a_bit = '{0:b}'.format(a)
    b_bit = '{0:b}'.format(b)
    if len(a_bit) > len(b_bit):
        len_offset = len(a_bit) - len(b_bit)
        b_bit = ("0" * len_offset) + b_bit
    else:
        len_offset = len(b_bit) - len(a_bit)
        a_bit = ("0" * len_offset) + a_bit
    return sum([1 for i in range(len(a_bit)) if a_bit[i] is not b_bit[i]])
'''

'''
def hammingDistance(a, b):
    a_bit = '{0:b}'.format(a)
    b_bit = '{0:b}'.format(b)
    if len(a_bit) > len(b_bit):
        main, other = a_bit, b_bit
    else:
        main, other = b_bit, a_bit
    offset = len(main) - (len(main) - len(other))
    count = 0
    isOverSmallLen = False
    result = 0
    # -1, -2, -3
    for i in range(-1, -1-len(main), -1):
        if isOverSmallLen:
            if main[i] == '1':
                result +=1
            continue
        if main[i] is not other[i]:
            result +=1
        count +=1
        if count == offset:
            isOverSmallLen = True
    return result
'''
assert hammingDistance(0,0) == 0
assert hammingDistance(2,1) == 2 #10, 01 = 2
assert hammingDistance(3,2), 1 #11, 10 = 1
assert hammingDistance(3,2), 1 #11, 10
assert hammingDistance(1,0), 1
assert hammingDistance(3,0), 2
assert hammingDistance(4,0), 3
assert hammingDistance(1,2), 2
assert hammingDistance(0,64), 6
assert hammingDistance(64,0), 6
