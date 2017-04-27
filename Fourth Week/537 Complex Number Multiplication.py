class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        a + a_virtural * b + b_virtual =
        a * b + a * b_virtual + b * a_virtural + a_virtural * b_virtual
        """
        a_num, a_virtual_num = a.split("+")
        b_num, b_virtual_num = b.split("+")
        a_num, b_num = int(a_num), int(b_num)
        a_virtual_number, b_virtual_number = int(a_virtual_num[:-1]), int(b_virtual_num[:-1])
        
        integer_number = a_num * b_num
        virtual_number = (a_num*b_virtual_number)+(b_num*a_virtual_number)
        double_virtual = (a_virtual_number*b_virtual_number)*-1
        number = integer_number + double_virtual
        return "{}+{}i".format(number, virtual_number)
        
        
s = Solution()

a, b = "1+1i", "1+1i"
assert s.complexNumberMultiply(a, b) == "0+2i"

a, b = "1+-1i", "1+-1i"
assert s.complexNumberMultiply(a, b) == "0+-2i"

a, b = "1+-1i", "0+0i"
assert s.complexNumberMultiply(a, b) == "0+0i"

